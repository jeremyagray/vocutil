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

"""vocutil CC multiple response tests."""

import json

import vocutil


def test_simple_mr():
    """Should produce a simple multiple response item."""
    questions = {
        "type": "multiple response",
        "question": "<p>This question has two correct answers.</p>",
        "answers": [
            {
                "answer": "correct",
                "correct": True,
            },
            {
                "answer": "right",
                "correct": True,
            },
            {
                "answer": "incorrect",
                "correct": False,
            },
            {
                "answer": "wrong",
                "correct": False,
            },
        ],
    }

    item = vocutil.cc.MultipleResponse(questions["question"], questions["answers"])

    actual = item.to_xml()

    expected = f"""<item ident="{str(item.uuid)}"><itemmetadata><qtimetadata><qtimetadatafield><fieldlabel>cc_profile</fieldlabel><fieldentry>cc.multiple_response.v0p1</fieldentry></qtimetadatafield></qtimetadata></itemmetadata><presentation><material><mattext texttype="text/html">&lt;p&gt;This question has two correct answers.&lt;/p&gt;</mattext></material><response_lid ident="{str(item.uuid)}" rcardinality="Multiple"><render_choice><response_label ident="{str(item.uuid)}-0"><material><mattext texttype="text/html">correct</mattext></material></response_label><response_label ident="{str(item.uuid)}-1"><material><mattext texttype="text/html">right</mattext></material></response_label><response_label ident="{str(item.uuid)}-2"><material><mattext texttype="text/html">incorrect</mattext></material></response_label><response_label ident="{str(item.uuid)}-3"><material><mattext texttype="text/html">wrong</mattext></material></response_label></render_choice></response_lid></presentation><resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal" /></outcomes><respcondition continue="No"><conditionvar><and><varequal respident="{str(item.uuid)}">{str(item.uuid)}-0</varequal><varequal respident="{str(item.uuid)}">{str(item.uuid)}-1</varequal><not><varequal respident="{str(item.uuid)}">{str(item.uuid)}-2</varequal></not><not><varequal respident="{str(item.uuid)}">{str(item.uuid)}-3</varequal></not></and></conditionvar><setvar action="Set" varname="SCORE">100</setvar></respcondition></resprocessing></item>"""  # noqa: E501

    assert actual == expected


def test_mr_json_roundtrip():
    """Should round-trip a multiple response with JSON."""
    questions = {
        "type": "multiple response",
        "question": "<p>This question has two correct answers.</p>",
        "answers": [
            {
                "answer": "correct",
                "correct": True,
            },
            {
                "answer": "right",
                "correct": True,
            },
            {
                "answer": "incorrect",
                "correct": False,
            },
            {
                "answer": "wrong",
                "correct": False,
            },
        ],
    }

    item = vocutil.cc.MultipleResponse(questions["question"], questions["answers"])

    print(item.to_xml())
    assert item.to_json() == json.dumps(questions)
