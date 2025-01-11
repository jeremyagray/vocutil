# ******************************************************************************
#
# vocutil, educational vocabulary utilities.
#
# Copyright 2022-2025 Jeremy A Gray <gray@flyquackswim.com>.
#
# All rights reserved.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# ******************************************************************************

"""vocutil module initialization."""

__version__ = "0.0.5"

from . import cc
from .create import create_unit
from .enrich import enrich
from .exceptions import VocutilError
from .load import _clean_glossary
from .load import _load_glossary_csv
from .load import _load_glossary_json
from .load import load_glossary
from .words import Entry
from .words import Glossary
