# Configuration file for the Sphinx documentation builder.

import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = 'ACTU-BASICS'
author = 'John GABARY'
copyright = '2024-2026, John GABARY'

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
    'sphinx_tabs.tabs',
    'sphinx_design',
]

language = 'fr'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output options -----------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_logo = "_static/actu-basics-logo-light.png"
html_favicon = "_static/actu-basics-logo-light.png"
html_sourcelink_suffix = ""
html_last_updated_fmt = ""
html_title = "ACTU-BASICS"

html_theme_options = {
    "header_links_before_dropdown": 5,
    "icon_links": [
        {
            "name": "YouTube (FR)",
            "url": "https://www.youtube.com/channel/UC3MrzU4G6UnSfDsYSci9BuQ",
            "icon": "fa-brands fa-youtube",
        },
        {
            "name": "YouTube (EN)",
            "url": "https://www.youtube.com/channel/UC9AkR6xNGl9S9XHuFnbFCGg",
            "icon": "fa-brands fa-youtube",
        },
        {
            "name": "TikTok (FR)",
            "url": "https://www.tiktok.com/@actu_basics_fr",
            "icon": "fa-brands fa-tiktok",
        },
        {
            "name": "TikTok (EN)",
            "url": "https://www.tiktok.com/@actu_basics",
            "icon": "fa-brands fa-tiktok",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/JohnGAB7",
            "icon": "fa-brands fa-github",
        },
    ],
    "logo": {
        "text": "ACTU-BASICS",
        "image_light": "_static/actu-basics-logo-light.png",
        "image_dark": "_static/actu-basics-logo-dark.png",
    },
    "use_edit_page_button": True,
    "show_toc_level": 2,
    "navbar_align": "left",
    "announcement": "Eveiller par les chiffres - Enlightening through numbers",
    "show_version_warning_banner": False,
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-version"],
}

html_context = {
    "github_user": "JohnGAB7",
    "github_repo": "Actu_Basics",
    "github_version": "main",
    "doc_path": "source",
}

html_static_path = ["_static"]
html_css_files = ["custom.css"]
todo_include_todos = True

# -- Autosummary / autodoc ---------------------------------------------------
autosummary_generate = True
autodoc_typehints = "description"
autodoc_member_order = "groupwise"

# -- Localization ------------------------------------------------------------
locale_dirs = ['locale/']
gettext_compact = False

# -- Napoleon ----------------------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_param = True
napoleon_use_rtype = True

# -- MathJax -----------------------------------------------------------------
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'

# -- LaTeX / epub ------------------------------------------------------------
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'figure_align': 'htbp',
}

epub_title = project
epub_exclude_files = ['search.html']
