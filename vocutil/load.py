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

"""vocutil loading functions."""

import csv

# import html
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
        except KeyError:
            cleaned["course"][entry] = ""

    # Book data.
    for entry in (
        "title",
        "author",
    ):
        try:
            cleaned["book"][entry] = data["book"][entry]
        except KeyError:
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
                except KeyError:
                    obj[entry] = ""

            cleaned["glossary"].append(obj)

    return cleaned


def _load_glossary_json(file):
    """Load a glossary."""
    with open(file, "r") as f:
        data = json.load(f)

    return clean_glossary(data)


def _load_glossary_csv(file, dialect="excel"):
    """Load a glossary in CSV."""
    with open(file, "r") as f:
        reader = csv.reader(f, dialect)
        data = {
            "glossary": [],
        }
        for row in reader:
            data["glossary"].append(
                {
                    "word": row[0],
                    "definition": row[1],
                }
            )

    return clean_glossary(data)


def _load_glossary_tsv(file):
    """Load a glossary in TSV."""
    return _load_glossary_csv(file, dialect="excel-tab")
