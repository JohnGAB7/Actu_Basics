# Configuration file for the Sphinx documentation builder.

import os
import sys
from pathlib import Path
from sphinx.application import Sphinx

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = 'ActuBasics'
author = 'John GABARY'
copyright = '2024, {John GABARY}'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.autosummary',
    'sphinx.ext.extlinks',
    'sphinx.ext.graphviz',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.httpdomain',
    'numpydoc', 
    #'sphinx_intl',
    'sphinx_tabs.tabs',
]

# Documentation language
language = 'fr'

# Template paths and exclusion patterns
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output options -----------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_logo = "_static/log.png"
html_favicon = "_static/log.png"
html_sourcelink_suffix = ""
html_last_updated_fmt = ""

# PyData theme customization
html_theme_options = {
    "header_links_before_dropdown": 4,
    "icon_links": [
        {
            "name": "Twitter",
            "url": "https://twitter.com/PyData",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/JohnGAB7",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Facebook",
            "url": "https://www.facebook.com/NivekJGL/",
            "icon": "fa-brands fa-facebook",
        },
        {
            "name": "Instagram",
            "url": "https://www.instagram.com/nivekjgl/",
            "icon": "fa-brands fa-instagram",
        },
        {
            "name": "YouTube",
            "url": "https://www.youtube.com/@Actu-Basics",
            "icon": "fa-brands fa-youtube",
        },
    ],
    "logo": {
        "text": "Actu-Basics",
        "image_dark": "_static/log2.png",
    },
    "use_edit_page_button": True,
    "show_toc_level": 10,
    "navbar_align": "left",
    "show_nav_level": 2 ,
    "announcement": "Bienvenue sur ma page destinée à l'apprentissage de logiciels pour L'Actuaire|Data Scientist",
    "show_version_warning_banner": True,
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-version"],
    "secondary_sidebar_items": {
        #"**/*": ["page-toc", "edit-this-page", "sourcelink"],
        "examples/no-sidebar": [],
    },
}

html_context = {
    "github_user": "pydata",
    "github_repo": "pydata-sphinx-theme",
    "github_version": "main",
    "doc_path": "docs",
}

rediraffe_redirects = {
    "contributing.rst": "community/index.rst",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["custom.css"]
todo_include_todos = True

# -- favicon options ---------------------------------------------------------

# see https://sphinx-favicon.readthedocs.io for more information about the
# sphinx-favicon extension
favicons = [
    # generic icons compatible with most browsers
    "favicon-32x32.png",
    "favicon-16x16.png",
    {"rel": "shortcut icon", "sizes": "any", "href": "favicon.ico"},
    # chrome specific
    "android-chrome-192x192.png",
    # apple icons
    {"rel": "mask-icon", "color": "#459db9", "href": "safari-pinned-tab.svg"},
    {"rel": "apple-touch-icon", "href": "apple-touch-icon.png"},
    # msapplications
    {"name": "msapplication-TileColor", "content": "#459db9"},
    {"name": "theme-color", "content": "#ffffff"},
    {"name": "msapplication-TileImage", "content": "mstile-150x150.png"},
]


# -- Options for autosummary/autodoc output ------------------------------------
autosummary_generate = True
autodoc_typehints = "description"
autodoc_member_order = "groupwise"

# -- Localization settings ---------------------------------------------------
locale_dirs = ['locale/']
gettext_compact = False

# -- Extensions configuration ------------------------------------------------

# Napoleon settings for docstring style
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_param = True
napoleon_use_rtype = True


# -- application setup -------------------------------------------------------


def setup_to_main(
    app: Sphinx, pagename: str, templatename: str, context, doctree
) -> None:
    """Add a function that jinja can access for returning an "edit this page" link pointing to `main`."""

    def to_main(link: str) -> str:
        """Transform "edit on github" links and make sure they always point to the main branch.

        Args:
            link: the link to the github edit interface

        Returns:
            the link to the tip of the main branch for the same file
        """
        links = link.split("/")
        idx = links.index("edit")
        return "/".join(links[: idx + 1]) + "/main/" + "/".join(links[idx + 2 :])

    context["to_main"] = to_main


def setup(app: Sphinx) -> Dict[str, Any]:
    """Add custom configuration to sphinx app.

    Args:
        app: the Sphinx application
    Returns:
        the 2 parallel parameters set to ``True``.
    """
    app.connect("html-page-context", setup_to_main)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }



# MathJax for mathematical notation
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'


# Graphviz and PlantUML settings
graphviz_output_format = 'svg'
inheritance_graph_attrs = dict(rankdir="LR", fontsize=14, ratio="compress")
plantuml = 'java -jar /path/to/plantuml.jar'  # Update the path to PlantUML

# -- LaTeX and other output formats ------------------------------------------

# Define the main document file (typically index.rst)

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'figure_align': 'htbp',
}

epub_title = project
epub_exclude_files = ['search.html']

# Optional back to top button in HTML
# "back_to_top_button": True, 

