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

"""vocutil loading functions."""

import json


def clean_glossary(data):
    """Clean a glossary."""
    cleaned = {
        "course": {},
        "book": {},
        "glossary": [],
    }

    # Course data.
    for entry in ("title",):
        try:
            cleaned["course"][entry] = data["course"][entry]
        except (KeyError):
            cleaned["course"][entry] = ""

    # Book data.
    for entry in (
        "title",
        "author",
    ):
        try:
            cleaned["book"][entry] = data["book"][entry]
        except (KeyError):
            cleaned["book"][entry] = ""

    # Glossary data.
    if "glossary" in data:
        for gloss in data["glossary"]:
            obj = {}
            for entry in (
                "word",
                "definition",
                "chapter",
                "section",
            ):
                try:
                    obj[entry] = gloss[entry]
                except (KeyError):
                    obj[entry] = ""

            cleaned["glossary"].append(obj)

    return cleaned


def load_glossary(file):
    """Load a glossary."""
    with open(file, "r") as f:
        data = json.load(f)

    return clean_glossary(data)
