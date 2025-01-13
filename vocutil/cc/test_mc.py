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

"""vocutil CC multiple choice tests."""

import json

import defusedxml.ElementTree as ET

import vocutil


def test_simple_mc():
    """Should produce a simple multiple choice item."""
    qdata = {
        "question": "<p>The three primary additive colors, when combined, will create this kind of light.</p>",  # noqa: E501
        "answers": [
            {
                "answer": "white",
                "correct": True,
            },
            {
                "answer": "black",
                "correct": False,
            },
            {
                "answer": "colorless",
                "correct": False,
            },
            {
                "answer": "clear",
                "correct": False,
            },
        ],
    }

    item = vocutil.cc.MultipleChoice(qdata["question"], qdata["answers"])

    actual = f"""<item ident="{str(item.uuid)}"><itemmetadata><qtimetadata><qtimetadatafield><fieldlabel>cc_profile</fieldlabel><fieldentry>cc.multiple_choice.v0p1</fieldentry></qtimetadatafield></qtimetadata></itemmetadata><presentation><material><mattext texttype="text/html">&lt;p&gt;The three primary additive colors, when combined, will create this kind of light.&lt;/p&gt;</mattext></material><response_lid ident="{str(item.uuid)}" rcardinality="Single"><render_choice><response_label ident="{str(item.uuid)}-0"><material><mattext texttype="text/html">white</mattext></material></response_label><response_label ident="{str(item.uuid)}-1"><material><mattext texttype="text/html">black</mattext></material></response_label><response_label ident="{str(item.uuid)}-2"><material><mattext texttype="text/html">colorless</mattext></material></response_label><response_label ident="{str(item.uuid)}-3"><material><mattext texttype="text/html">clear</mattext></material></response_label></render_choice></response_lid></presentation><resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal" /></outcomes><respcondition continue="No"><conditionvar><varequal respident="{str(item.uuid)}">{str(item.uuid)}-0</varequal></conditionvar><setvar action="Set" varname="SCORE">100</setvar></respcondition></resprocessing></item>"""  # noqa: E501

    expected = ET.tostring(
        item.item,
        encoding="unicode",
    )

    assert actual == expected


def test_mc_json_roundtrip():
    """Should produce a simple multiple choice item."""
    qdata = {
        "question": "<p>The three primary additive colors, when combined, will create this kind of light.</p>",  # noqa: E501
        "answers": [
            {
                "answer": "white",
                "correct": True,
            },
            {
                "answer": "black",
                "correct": False,
            },
            {
                "answer": "colorless",
                "correct": False,
            },
            {
                "answer": "clear",
                "correct": False,
            },
        ],
    }

    item = vocutil.cc.MultipleChoice(qdata["question"], qdata["answers"])

    assert item.to_json() == json.dumps(qdata)


def test_mc_xml_roundtrip():
    """Should roundtrip with XML."""
    qdata = {
        "question": "<p>The three primary additive colors, when combined, will create this kind of light.</p>",  # noqa: E501
        "answers": [
            {
                "answer": "white",
                "correct": True,
            },
            {
                "answer": "black",
                "correct": False,
            },
            {
                "answer": "colorless",
                "correct": False,
            },
            {
                "answer": "clear",
                "correct": False,
            },
        ],
    }

    item = vocutil.cc.MultipleChoice(qdata["question"], qdata["answers"])
    xml_str = item.to_xml()
    xml_item = vocutil.cc.MultipleChoice.from_xml(xml_str)

    assert item.question == xml_item.question
