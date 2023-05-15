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

"""vocutil CC multiple choice tests."""

import sys
import xml.etree.ElementTree as ET

# import pytest

sys.path.insert(0, "/home/gray/src/work/vocutil")

import vocutil  # noqa: E402


def test_correct_xml():
    """Should produce correct XML."""
    qdata = {
        "question": "<p>The three primary additive colors, when combined, will create this kind of light.</p>",
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

    actual = """<item ident="1"><itemmetadata><qtimetadata><qtimetadatafield><fieldlabel>cc_profile</fieldlabel><fieldentry>cc.multiple_choice.v0p1</fieldentry></qtimetadatafield></qtimetadata></itemmetadata><presentation><material><mattext texttype="text/html">&lt;p&gt;The three primary additive colors, when combined, will create this kind of light.&lt;/p&gt;</mattext></material><response_lid ident="1" rcardinality="Single"><render_choice><response_label ident="1-0"><material><mattext texttype="text/plain">white</mattext></material></response_label><response_label ident="1-1"><material><mattext texttype="text/plain">black</mattext></material></response_label><response_label ident="1-2"><material><mattext texttype="text/plain">colorless</mattext></material></response_label><response_label ident="1-3"><material><mattext texttype="text/plain">clear</mattext></material></response_label></render_choice></response_lid></presentation><resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal" /></outcomes><respcondition continue="No"><conditionvar><varequal respident="1">1-0</varequal></conditionvar><setvar action="Set" varname="SCORE">100</setvar></respcondition></resprocessing></item>"""
    expected = ET.tostring(vocutil.cc.MultipleChoice(qdata, ident="1").item, encoding="unicode")

    assert actual == expected
