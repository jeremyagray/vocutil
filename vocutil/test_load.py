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

"""vocutil loading tests."""

import sys

import pytest

sys.path.insert(0, "/home/gray/src/work/vocutil")

import vocutil  # noqa: E402


def test_clean_glossary():
    """Should clean a glossary."""
    data = {
        "course": {
            "title": "Course A",
        },
        "book": {
            "title": "A Textbook",
            "author": "J Gray",
        },
        "glossary": [
            {
                "word": "test",
                "definition": "a test",
                "chapter": 1,
                "section": 1,
            },
        ],
    }

    assert data == vocutil.clean_glossary(data)
