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

"""Common Cartridge fill-in-the-blank item."""

import json
from xml.etree.ElementTree import Element as ETElement  # nosec B405
from xml.etree.ElementTree import SubElement as ETSubElement  # nosec B405

import defusedxml.ElementTree as ET

from .item import Item


class FillInTheBlank(Item):
    """A Common Cartridge fill in the blank item."""

    def __init__(self, question, answers, default_case="No", **kwargs):
        """Initialize a ``FillInTheBlank`` item.

        Initialize a ``FillInTheBlank`` item.

        Parameters
        ----------
        question : str
            The HTML formatted question text.
        answers : [obj]
            The correct answer(s).
        """
        # Call the super.
        super().__init__(**kwargs)

        self.question = question
        self.answers = answers
        self.default_case = default_case if default_case == "Yes" else "No"

        self.item = ETElement("item", ident=str(self.uuid))
        self.itemmetadata = ETSubElement(self.item, "itemmetadata")
        self.qtimetadata = ETSubElement(self.itemmetadata, "qtimetadata")
        self.qtimetadatafield = ETSubElement(self.qtimetadata, "qtimetadatafield")
        self.fieldlabel = ETSubElement(self.qtimetadatafield, "fieldlabel")
        self.fieldlabel.text = "cc_profile"
        self.fieldentry = ETSubElement(self.qtimetadatafield, "fieldentry")
        self.fieldentry.text = "cc.fib.v0p1"
        self.presentation = ETSubElement(self.item, "presentation")
        self.material = ETSubElement(self.presentation, "material")
        self.mattext = ETSubElement(self.material, "mattext", texttype="text/html")
        self.mattext.text = self.question

        self.response = ETSubElement(
            self.presentation,
            "response_str",
            rcardinality="Single",
            ident=f"fib-resp-{str(self.uuid)}",
        )
        self.blank = ETSubElement(self.response, "render_fib", prompt="Dashline")

        grade = ETSubElement(self.item, "resprocessing")
        outcomes = ETSubElement(grade, "outcomes")
        ETSubElement(
            outcomes,
            "decvar",
            maxvalue="100",
            minvalue="0",
            varname="SCORE",
            vartype="Decimal",
        )
        cond = ETSubElement(
            grade,
            "respcondition",
            attrib={
                "continue": "No",
            },
        )
        condvar = ETSubElement(cond, "conditionvar")

        # Set possible correct answers.
        for answer in self.answers:
            varequal = ETSubElement(
                condvar,
                "varequal",
                case=answer["case"] if "case" in answer else self.default_case,
                respident=f"fib-resp-{str(self.uuid)}",
            )
            varequal.text = answer["answer"]

        setvar = ETSubElement(cond, "setvar", action="Set", varname="SCORE")
        setvar.text = "100"

        return

    @classmethod
    def from_json(cls, item, **kwargs):
        """Create a ``FillInTheBlank`` item from JSON data.

        Create a ``FillInTheBlank`` item from JSON fill-in-the-blank
        item data.

        Parameters
        ----------
        cls
            The ``FillInTheBlank`` class.
        item : str
            A string containing JSON fill-in-the-blank data.
        """
        data = json.loads(item)

        return cls(data["question"], data["answers"], **kwargs)

    @classmethod
    def from_xml(cls, item, **kwargs):
        """Create a ``FillInTheBlank`` item XML data.

        Create a ``FillInTheBlank`` item from IMSCC fill-in-the-blank
        XML data.

        Parameters
        ----------
        cls
            The ``FillInTheBlank`` class.
        item : str
            A string containing IMSCC fill-in-the-blank XML data.
        """
        tree = ET.fromstring(item)

        # Question text.
        q = tree.find("presentation").find("material").find("mattext").text

        # Correct answers.
        a = [
            {
                "answer": ele.text,
                "case": ele.get("case"),
            }
            for ele in tree.find("resprocessing")
            .find("respcondition")
            .find("conditionvar")
            .findall("varequal")
        ]

        return cls(q, a, **kwargs)

    def to_json(self):
        """Create a fill-in-the-blank JSON string from item data."""
        return json.dumps(
            {
                "question": str(self.mattext.text),
                "answers": [
                    {
                        "answer": ele.text,
                        "case": ele.get("case"),
                    }
                    for ele in self.item.find("resprocessing")
                    .find("respcondition")
                    .find("conditionvar")
                    .findall("varequal")
                ],
            }
        )

    def to_xml(self):
        """Create a fill-in-the-blank XML string from item data."""
        return ET.tostring(self.item, encoding="unicode")
