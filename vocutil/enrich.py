# ******************************************************************************
#
# vocutil, educational vocabulary utilities.
#
# Copyright 2022-2023 Jeremy A Gray <gray@flyquackswim.com>.
#
# All rights reserved.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# ******************************************************************************

"""Combine glossary and course data."""

import json
import sys

from .load import load_glossary


def enrich():
    """Combine glossary and course data."""
    data = load_glossary(sys.argv[1])
    chapter = int(sys.argv[2])
    glossary_fns = sys.argv[3:]

    for fn in glossary_fns:
        gl = load_glossary(fn)
        for entry in gl["glossary"]:
            data["glossary"].append(
                {
                    "word": entry["word"] if "word" in entry else "",
                    "definition": entry["definition"] if "definition" in entry else "",
                    "chapter": str(entry["chapter"])
                    if "chapter" in entry and entry["chapter"]
                    else str(chapter),
                    "section": str(entry["section"])
                    if "section" in entry and entry["section"]
                    else "",
                }
            )

    print(json.dumps(data, indent=2))
