# -- Path setup

# -- Project information
project = "sphinxcontrib-budoux"
copyright = "2022, Kazuya Takei"
author = "Kazuya Takei"
release = "0.1.2"
language = "ja"

# -- General configuration
extensions = [
    "sphinx.ext.intersphinx",
    "sphinxcontrib.budoux",
    "sphinx_rtd_theme",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
