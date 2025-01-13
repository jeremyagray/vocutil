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

"""vocutil Common Cartridge multiple choice tests."""

import json

import vocutil


def test_simple_tf():
    """Should produce a simple true/false item."""
    qdata = {
        "question": "<p>One is one more than zero.</p>",
        "answer": True,
    }

    item = vocutil.cc.TrueFalse(qdata["question"], qdata["answer"])

    actual = item.to_xml()

    expected = f"""<item ident="{str(item.uuid)}"><itemmetadata><qtimetadata><qtimetadatafield><fieldlabel>cc_profile</fieldlabel><fieldentry>cc.true_false.v0p1</fieldentry></qtimetadatafield></qtimetadata></itemmetadata><presentation><material><mattext texttype="text/html">&lt;p&gt;One is one more than zero.&lt;/p&gt;</mattext></material><response_lid ident="{str(item.uuid)}" rcardinality="Single"><render_choice><response_label ident="{str(item.uuid)}-01"><material><mattext texttype="text/plain">True</mattext></material></response_label><response_label ident="{str(item.uuid)}-02"><material><mattext texttype="text/plain">False</mattext></material></response_label></render_choice></response_lid></presentation><resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal" /></outcomes><respcondition continue="No"><conditionvar><varequal respident="{str(item.uuid)}">{str(item.uuid)}-01</varequal></conditionvar><setvar action="Set" varname="SCORE">100</setvar></respcondition></resprocessing></item>"""  # noqa: E501

    assert actual == expected


def test_tf_init_should_roundtrip_json():
    """Should round-trip with JSON via ``__init__``."""
    qdata = {
        "question": "<p>One is one more than zero.</p>",
        "answer": True,
    }

    item = vocutil.cc.TrueFalse(qdata["question"], qdata["answer"])

    assert item.to_json() == json.dumps(qdata)


def test_tf_cls_should_roundtrip_json():
    """Should round-trip with JSON via class method."""
    qdata = {
        "question": "<p>One is one more than zero.</p>",
        "answer": True,
    }

    item = vocutil.cc.TrueFalse.from_json(json.dumps(qdata))

    assert item.to_json() == json.dumps(qdata)


def test_tf_init_should_roundtrip_xml():
    """Should round-trip with XML."""
    qdata = {
        "question": "<p>One is one more than zero.</p>",
        "answer": True,
    }

    item = vocutil.cc.TrueFalse(qdata["question"], qdata["answer"])

    xml_str = item.to_xml()
    xml_item = vocutil.cc.TrueFalse.from_xml(xml_str)

    assert item.question == xml_item.question
