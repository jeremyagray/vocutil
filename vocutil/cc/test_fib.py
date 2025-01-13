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

import vocutil


def test_one_correct_response_case_insensitive():
    """Should produce correct XML for one correct, case insensitive response."""
    qdata = {
        "question": "<p>_:  the process of separating a wave of different frequencies into its individual component waves</p>",  # noqa: E501
        "answers": [
            {
                "answer": "dispersion",
                "case": "No",
            },
        ],
    }

    item = vocutil.cc.FillInTheBlank(
        qdata["question"],
        qdata["answers"],
    )

    actual = item.to_xml()

    expected = f"""<item ident="{str(item.uuid)}"><itemmetadata><qtimetadata><qtimetadatafield><fieldlabel>cc_profile</fieldlabel><fieldentry>cc.fib.v0p1</fieldentry></qtimetadatafield></qtimetadata></itemmetadata><presentation><material><mattext texttype="text/html">&lt;p&gt;_:  the process of separating a wave of different frequencies into its individual component waves&lt;/p&gt;</mattext></material><response_str rcardinality="Single" ident="fib-resp-{str(item.uuid)}"><render_fib prompt="Dashline" /></response_str></presentation><resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal" /></outcomes><respcondition continue="No"><conditionvar><varequal case="No" respident="fib-resp-{str(item.uuid)}">dispersion</varequal></conditionvar><setvar action="Set" varname="SCORE">100</setvar></respcondition></resprocessing></item>"""  # noqa: E501

    assert actual == expected


def test_one_correct_response_case_sensitive():
    """Should produce correct XML for one correct, case sensitive response."""
    qdata = {
        "question": "<p>_:  the process of separating a wave of different frequencies into its individual component waves</p>",  # noqa: E501
        "answers": [
            {
                "answer": "dispersion",
                "case": "Yes",
            },
        ],
    }

    item = vocutil.cc.FillInTheBlank(
        qdata["question"],
        qdata["answers"],
    )

    actual = item.to_xml()

    expected = f"""<item ident="{str(item.uuid)}"><itemmetadata><qtimetadata><qtimetadatafield><fieldlabel>cc_profile</fieldlabel><fieldentry>cc.fib.v0p1</fieldentry></qtimetadatafield></qtimetadata></itemmetadata><presentation><material><mattext texttype="text/html">&lt;p&gt;_:  the process of separating a wave of different frequencies into its individual component waves&lt;/p&gt;</mattext></material><response_str rcardinality="Single" ident="fib-resp-{str(item.uuid)}"><render_fib prompt="Dashline" /></response_str></presentation><resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal" /></outcomes><respcondition continue="No"><conditionvar><varequal case="Yes" respident="fib-resp-{str(item.uuid)}">dispersion</varequal></conditionvar><setvar action="Set" varname="SCORE">100</setvar></respcondition></resprocessing></item>"""  # noqa: E501

    assert actual == expected


def test_two_correct_responses_case_insensitive():
    """Should produce correct XML for two correct, case insensitive responses."""
    qdata = {
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

    item = vocutil.cc.FillInTheBlank(
        qdata["question"],
        qdata["answers"],
    )

    actual = item.to_xml()

    expected = f"""<item ident="{str(item.uuid)}"><itemmetadata><qtimetadata><qtimetadatafield><fieldlabel>cc_profile</fieldlabel><fieldentry>cc.fib.v0p1</fieldentry></qtimetadatafield></qtimetadata></itemmetadata><presentation><material><mattext texttype="text/html">&lt;p&gt;_:  the process of separating a wave of different frequencies into its individual component waves&lt;/p&gt;</mattext></material><response_str rcardinality="Single" ident="fib-resp-{str(item.uuid)}"><render_fib prompt="Dashline" /></response_str></presentation><resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal" /></outcomes><respcondition continue="No"><conditionvar><varequal case="No" respident="fib-resp-{str(item.uuid)}">dispersion</varequal><varequal case="No" respident="fib-resp-{str(item.uuid)}">dispersions</varequal></conditionvar><setvar action="Set" varname="SCORE">100</setvar></respcondition></resprocessing></item>"""  # noqa: E501

    assert actual == expected


def test_two_correct_responses_case_sensitive():
    """Should produce correct XML for two correct, case sensitive responses."""
    qdata = {
        "question": "<p>_:  the process of separating a wave of different frequencies into its individual component waves</p>",  # noqa: E501
        "answers": [
            {
                "answer": "dispersion",
                "case": "Yes",
            },
            {
                "answer": "dispersions",
                "case": "Yes",
            },
        ],
    }

    item = vocutil.cc.FillInTheBlank(
        qdata["question"],
        qdata["answers"],
    )

    actual = item.to_xml()

    expected = f"""<item ident="{str(item.uuid)}"><itemmetadata><qtimetadata><qtimetadatafield><fieldlabel>cc_profile</fieldlabel><fieldentry>cc.fib.v0p1</fieldentry></qtimetadatafield></qtimetadata></itemmetadata><presentation><material><mattext texttype="text/html">&lt;p&gt;_:  the process of separating a wave of different frequencies into its individual component waves&lt;/p&gt;</mattext></material><response_str rcardinality="Single" ident="fib-resp-{str(item.uuid)}"><render_fib prompt="Dashline" /></response_str></presentation><resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal" /></outcomes><respcondition continue="No"><conditionvar><varequal case="Yes" respident="fib-resp-{str(item.uuid)}">dispersion</varequal><varequal case="Yes" respident="fib-resp-{str(item.uuid)}">dispersions</varequal></conditionvar><setvar action="Set" varname="SCORE">100</setvar></respcondition></resprocessing></item>"""  # noqa: E501

    assert actual == expected
