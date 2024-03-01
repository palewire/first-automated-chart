"""Configuration file for the Sphinx documentation builder."""
from datetime import datetime
from typing import Any

project = "First Automated Chart"
year = datetime.now().year
copyright = f"{year} palewire"
author = "palewire"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "palewire"
pygments_style = "sphinx"

html_sidebars: dict[Any, Any] = {}
html_theme_options: dict[Any, Any] = {
    "canonical_url": "https://palewi.re/docs/first-automated-chart/",
    "nosidebar": True,
}

autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "show-inheritance": True,
}

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinxcontrib.mermaid",
]
