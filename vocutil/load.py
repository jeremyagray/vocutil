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
import json

from .exceptions import VocutilError


def load_glossary(fn):
    """Load a glossary.

    Load a glossary in vocutil JSON or word/definition CSV/TSV.

    fn : str
        The filename containing the glossary data.
    """
    try:
        return _load_glossary_json(fn)
    except json.JSONDecodeError:
        pass

    try:
        return _load_glossary_csv(fn)
    except csv.Error:
        raise VocutilError("Unable to parse glossary data.")


def _clean_glossary(data):
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

    return _clean_glossary(data)


def _load_glossary_csv(fn):
    """Load a glossary in CSV."""
    with open(fn, "r") as f:
        # Detect CSV dialect and reset file object.
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(f.readline())
        f.seek(0)

        # Read CSV file and populate glossary.
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

    return _clean_glossary(data)
