# Copyright © 2020 Hartmut Goebel <h.goebel@crazy-compilers.com>
#
# This file is part of PyInstaller Hook Sample.
#
# PyInstaller Hook Sample is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3 of
# the License, or (at your option) any later version.
#
# PyInstaller Hook Sample is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with the PyInstaller Hook Sample. If not, see
# <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys, os
import sphinx_rtd_theme
import CodeChat.CodeToRest
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'PyInstaller Hooksample'
copyright = '2020, the PyInstaller Development Team'
author = 'PyInstaller Development Team'

# Short version
version = "0.0"
# The full version, including alpha/beta/rc tags
release = '0.0'


# -- General configuration ---------------------------------------------------

# A string of reStructuredText that will be included at the end of every source
# file that is read.
rst_epilog = (
    # Provide a convenient way to refer to a source file's name.
    """

.. |docname| replace:: :docname:`name`
""")

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "CodeChat.CodeToRestSphinx",
    "sphinx_rtd_theme"
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
#
# **Important:** Do **NOT** add ``CodeChat.css`` to this list; this will
# instruct Sphinx not to copy it to the ``_static`` directory, where it
# is needed to properly lay out CodeChat output.
exclude_patterns = [
    # Misc files.
    "Thumbs.db",
    ".DS_Store",
    "_build",
    "README.rst",
    "build",
    "dist",
    "_venv",
    ".tox",
    ".pytest_cache",
    "**/.pytest_cache",
    "**/*.egg-info",
    # editor artifacts
    "sphinx-enki-info.txt",
    # A file used by the program, but not for documentation.
    "src/pyi_hooksample/message.txt",
    #
    'conf.py',
    '.gitignore',
    '*requirements.txt',
    'Makefile',
    'setup.py',
    '*.bat',
    'readthedocs.yml',
    'MANIFEST.in',
]

# The suffix of source filenames.
source_suffix = ".rst"

# master toctree document.
master_doc = "index"

# `keep_warnings: If true, keep warnings as "system message"
# paragraphs in the built documents. **CodeChat note**: This should
# always be True; doing so places warnings next to the offending text
# in the web view, making them easy to find and fix.
keep_warnings = True

# -- Options for CodeChat processing -----------------------------------------

# `CodeChat_lexer_for_glob` is a dict of {glob_, lexer_alias}, which
# uses lexer_alias (e.g. a pygments lexer's `short name) to analyze
# any file which matches the given glob-style pattern.
CodeChat_lexer_for_glob = {
    # CSS files are auto-detected as a CSS + Lasso file by Pygments,
    # causing it to display incorrectly. Define them as CSS only.
    "*.css": "CSS",

    # These files use ``#`` as a comment. So does Perl. Ugly...
    "MANIFEST.in": "Perl",
    ".gitignore": "Perl",
    "*.cfg": "Perl",
    "*.dat": "Perl",
    "*.txt": "Perl",
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# `html_static_path <http://sphinx-doc.org/config.html#confval-html_static_path>`_:
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files, so
# a file named ``default.css`` will overwrite the builtin ``default.css``.
# **CodeChat note:** Include the path to CodeChat's static files.
html_static_path = CodeChat.CodeToRest.html_static_path()

# Fix up styles for the ReadTheDocs theme.
html_css_files = ['CodeChat_sphinx_rtd_theme.css']

# Insert a 'Last updated on:' timestamp at every page bottom.
html_last_updated_fmt = "%Y-%m-%d"

html_copy_source = False
html_show_sourcelink = False
