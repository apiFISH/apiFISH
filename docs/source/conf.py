# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
import apifish

# Sphinx import all module with autodoc but don't need these modules to build API doc
autodoc_mock_imports = [
    "pympler",
    "dask",
    "tqdm",
    "astropy",
    "tifffile",
    "scipy",
    "sklearn",
    "photutils",
    "stardist",
    "csbdeep",
    "numba",
    "pylab",
    "skimage",
]

project = "apiFISH"
copyright = "2024, Arthur Imbert, Marcelo Nollmann, Xavier Devos"
author = "Arthur Imbert, Marcelo Nollmann, Xavier Devos"
release = "0.7.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # include documentation from docstring
    "sphinx.ext.napoleon",  # allow google or numpy docstring
    "myst_parser",  # parse markdown files to be understood by sphinx
    "sphinx_panels",  # for creating panels like pandas or numpy main doc page
    "nbsphinx",  # include jupyter notebook file, WARNING: uncompatible with mermaid on ReadTheDocs
    "IPython.sphinxext.ipython_console_highlighting",  # Resolve highlighting "literal_block" bug
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "**.ipynb_checkpoints"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = "sphinx_book_theme"

html_context = {"default_mode": "light"}

html_theme_options = {
    "repository_url": "https://github.com/apiFISH/apiFISH",
    "use_repository_button": True,
    "use_edit_page_button": False,
    "path_to_docs": "docs",
    "logo_only": True,
}

html_logo = "_static/logo_apiFISH.png"

html_static_path = ["_static"]

myst_heading_anchors = 2
