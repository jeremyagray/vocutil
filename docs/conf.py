# ******************************************************************************
#
# vocutil, educational vocabulary utilities.
#
# Copyright 2022 Jeremy A Gray <gray@flyquackswim.com>.
#
# All rights reserved.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# ******************************************************************************

"""Sphinx documentation configuration."""

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "vocutil"
copyright = "2022, Jeremy A Gray"
author = "Jeremy A Gray"
release = "0.0.1"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
]

autosummary_generate = True

# All paths relative to this directory.
templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]
html_static_path = ["_static"]

html_theme = "alabaster"
