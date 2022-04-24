import budoux
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)


def apply_budoux(app: Sphinx, page_name, template_name, context, doctree):
    if "body" not in context:
        return

    def rebuild_title(content: str):
        parser = budoux.load_default_japanese_parser()
        tag = Tag(name=app.config.budoux_split_tag, can_be_empty_element=True)
        return sum([[NavigableString(text), tag] for text in parser.parse(content)], [])

    soup = BeautifulSoup(context["body"], "html.parser")
    for tag in app.config.budoux_targets:
        for elm in soup.find_all(tag):
            new_title = rebuild_title(elm.contents[0])
            elm.attrs["style"] = app.config.budoux_split_style
            elm.contents = new_title[:-1] + elm.contents[1:]
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
