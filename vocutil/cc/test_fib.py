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

"""vocutil Common Cartridge fill-in-the-blank tests."""

import json
import pytest
import vocutil


def test__canonicalize_case_should_handle_good_values():
    """Should handle good values."""
    assert vocutil.cc._canonicalize_case("Yes") == "Yes"
    assert vocutil.cc._canonicalize_case("yes") == "Yes"
    assert vocutil.cc._canonicalize_case(True) == "Yes"
    assert vocutil.cc._canonicalize_case(1) == "Yes"
    assert vocutil.cc._canonicalize_case("No") == "No"
    assert vocutil.cc._canonicalize_case("no") == "No"
    assert vocutil.cc._canonicalize_case(False) == "No"
    assert vocutil.cc._canonicalize_case(0) == "No"


def test__canonicalize_case_should_raise_on_bad_values():
    """Should raise on bad values."""
    with pytest.raises(ValueError):
        vocutil.cc._canonicalize_case("sensitive")


def test_fib_should_produce_correct_xml():
    """Should produce correct XML."""
    data = {
        "type": "fib",
        "question": "<p>_:  the process of separating a wave of different frequencies into its individual component waves</p>",  # noqa: E501
        "answers": [
            {
                "answer": "dispersion",
                "case": "No",
            },
        ],
    }

    item = vocutil.cc.FillInTheBlank(
        data["question"],
        data["answers"],
    )

    actual = item.to_xml()

    expected = f"""<item ident="{item.uuid!s}"><itemmetadata><qtimetadata><qtimetadatafield><fieldlabel>cc_profile</fieldlabel><fieldentry>cc.fib.v0p1</fieldentry></qtimetadatafield></qtimetadata></itemmetadata><presentation><material><mattext texttype="text/html">&lt;p&gt;_:  the process of separating a wave of different frequencies into its individual component waves&lt;/p&gt;</mattext></material><response_str rcardinality="Single" ident="fib-resp-{item.uuid!s}"><render_fib prompt="Dashline" /></response_str></presentation><resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal" /></outcomes><respcondition continue="No"><conditionvar><varequal case="No" respident="fib-resp-{item.uuid!s}">dispersion</varequal></conditionvar><setvar action="Set" varname="SCORE">100</setvar></respcondition></resprocessing></item>"""  # noqa: E501

    assert actual == expected


def test_fib_from_json_should_roundtrip():
    """Should roundrip JSON."""
    data = {
        "type": "fib",
        "question": "<p>_:  the process of separating a wave of different frequencies into its individual component waves</p>",  # noqa: E501
        "answers": [
            {
                "answer": "dispersion",
                "case": "No",
            },
            {
                "answer": "dispersions",
                "case": "No",
            },
        ],
    }

    assert (
        json.loads(vocutil.cc.FillInTheBlank.from_json(json.dumps(data)).to_json())
        == data
    )


def test_fib_from_xml_should_roundtrip():
    """Should roundrip XML."""
    data = {
        "type": "fib",
        "question": "<p>_:  the process of separating a wave of different frequencies into its individual component waves</p>",  # noqa: E501
        "answers": [
            {
                "answer": "dispersion",
                "case": "No",
            },
            {
                "answer": "dispersions",
                "case": "No",
            },
        ],
    }

    one = vocutil.cc.FillInTheBlank(data["question"], data["answers"])
    two = vocutil.cc.FillInTheBlank.from_xml(one.to_xml())

    assert one.question == two.question
    assert one.answers == two.answers
