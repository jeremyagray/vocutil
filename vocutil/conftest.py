# ******************************************************************************
#
# vocutil, educational vocabulary utilities.
#
# Copyright 2022-2024 Jeremy A Gray <gray@flyquackswim.com>.
#
# All rights reserved.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# ******************************************************************************

"""vocutil tests fixture data."""

import pytest


@pytest.fixture(
    params=[
        {
            "text": """1) According to the Ptolemaic (Greek) model of the universe, how many "heavenly" bodies could be observed wandering along the background of stars?
A) one
B) two
C) five
D) seven
Answer:  D
Diff: 1
Topic:  21.1 Ancient Astronomy
Bloom's Taxonomy:  Knowledge/Comprehension
""",  # noqa E501
            "question": """According to the Ptolemaic (Greek) model of the universe, how many "heavenly" bodies could be observed wandering along the background of stars?""",  # noqa E501
            "chapter": "21",
            "section": "1",
            "answer": 3,
        },
        {
            "text": """2) This is also a question?
A) a
B) b
C) c
D) d
Answer:  B
Diff: 7
Topic:  25.7 Test
Bloom's Taxonomy:  Knowledge/Comprehension
""",
            "question": """This is also a question?""",
            "chapter": "25",
            "section": "7",
            "answer": 1,
        },
    ]
)
def question_data(request):
    """Parseable texts."""
    return request.param


@pytest.fixture(
    params=[
        "",
        "empty",
        " ",
        "	",
    ]
)
def unparseable(request):
    """Unparseable texts."""
    return request.param


@pytest.fixture(
    params=[
        "nofile.txt",
        "nofile.docx",
        "",
        " ",
        "	",
    ]
)
def badfn(request):
    """Bad file names."""
    return request.param
