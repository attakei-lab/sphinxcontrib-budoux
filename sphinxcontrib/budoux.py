from functools import lru_cache

import budoux
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util import logging

logger = logging.getLogger(__name__)


def rebuild_contents(elm: Tag, config: Config):
    parser = lru_cache(maxsize=None)(budoux.load_default_japanese_parser)()
    tag = Tag(name=config.budoux_split_tag, can_be_empty_element=True)
    contents = []
    for content in elm.contents:
        if not isinstance(content, NavigableString):
            contents.append(content)
            continue
        tokens = parser.parse(content)
        contents += sum([[NavigableString(token), tag] for token in tokens], [])
    return contents


def apply_budoux(app: Sphinx, page_name, template_name, context, doctree):
    if "body" not in context:
        return

    soup = BeautifulSoup(context["body"], "html.parser")
    for tag in app.config.budoux_targets:
        for elm in soup.find_all(tag):
            elm.attrs["style"] = app.config.budoux_split_style
            elm.contents = rebuild_contents(elm, app.config)
    context["body"] = soup
    return


def setup(app: Sphinx):
    """
    Setup function for this extension.
    """
    logger.debug(f"Using {__name__}")
    app.add_config_value("budoux_split_tag", "wbr", "env")
    app.add_config_value(
        "budoux_split_style", "word-break: keep-all; overflow-wrap: break-word;", "env"
    )
    app.add_config_value("budoux_targets", ["h1"], "env")
    app.connect("html-page-context", apply_budoux)
