from io import StringIO

import pytest
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html")
def test_default(app: SphinxTestApp, status: StringIO, warning: StringIO):
    app.build()
    out_html = app.outdir / "index.html"
    soup = BeautifulSoup(out_html.read_text(), "html.parser")
    h1 = soup.h1
    contents = list(h1.children)
    assert len(list(h1.children)) > 1
    assert "word-break: keep-all; overflow-wrap: break-word;" in h1["style"]
    assert isinstance(contents[0], NavigableString)
    assert isinstance(contents[1], Tag)
    assert contents[1].name == "wbr"
    assert len(list(soup.h2.children)) == 1


@pytest.mark.sphinx("html", confoverrides={"budoux_targets": ["h1", "h2"]})
def test_multiple_targets(app: SphinxTestApp, status: StringIO, warning: StringIO):
    app.build()
    out_html = app.outdir / "index.html"
    soup = BeautifulSoup(out_html.read_text(), "html.parser")
    assert len(list(soup.h1.children)) > 1
    assert len(list(soup.h2.children)) > 1
