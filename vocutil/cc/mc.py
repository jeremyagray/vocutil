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

"""Common Cartridge multiple choice item."""

import json
from xml.etree.ElementTree import Element as ETElement  # nosec B405
from xml.etree.ElementTree import SubElement as ETSubElement  # nosec B405

import defusedxml.ElementTree as ET

from .item import Item


class MultipleChoice(Item):
    """A Common Cartridge multiple choice item."""

    def __init__(self, question, answers, **kwargs):
        """Initialize a ``MultipleChoice`` item.

        Initialize a ``MultipleChoice`` item.

        Parameters
        ----------
        question : str
            The HTML formatted question text.
        answers : [obj]
            The possible answers.
        """
        # Call the super.
        super().__init__(**kwargs)

        self.question = question
        self.answers = answers
        self.item = ETElement("item", ident=str(self.uuid))
        self.itemmetadata = ETSubElement(self.item, "itemmetadata")
        self.qtimetadata = ETSubElement(self.itemmetadata, "qtimetadata")
        self.qtimetadatafield = ETSubElement(self.qtimetadata, "qtimetadatafield")
        self.fieldlabel = ETSubElement(self.qtimetadatafield, "fieldlabel")
        self.fieldlabel.text = "cc_profile"
        self.fieldentry = ETSubElement(self.qtimetadatafield, "fieldentry")
        self.fieldentry.text = "cc.multiple_choice.v0p1"
        self.presentation = ETSubElement(self.item, "presentation")
        self.material = ETSubElement(self.presentation, "material")
        self.mattext = ETSubElement(self.material, "mattext", texttype="text/html")
        self.mattext.text = question

        self.response = ETSubElement(
            self.presentation,
            "response_lid",
            ident=str(self.uuid),
            rcardinality="Single",
        )
        self.choices = ETSubElement(self.response, "render_choice")

        correct = None
        for i, ans in enumerate(answers):
            ident = f"{self.uuid}-{i}"
            choice = ETSubElement(self.choices, "response_label", ident=ident)
            material = ETSubElement(choice, "material")
            mattext = ETSubElement(material, "mattext", texttype="text/html")
            mattext.text = ans["answer"]
            if ans["correct"]:
                correct = ident

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
        varequal = ETSubElement(condvar, "varequal", respident=str(self.uuid))
        varequal.text = correct
        setvar = ETSubElement(cond, "setvar", action="Set", varname="SCORE")
        setvar.text = "100"

        return

    @classmethod
    def from_json(cls, item, **kwargs):
        """Create a ``MultipleChoice`` item from JSON data.

        Create a ``MultipleChoice`` item from JSON data.

        Parameters
        ----------
        cls
            The ``MultipleChoice`` class.
        item : str
            A string containing JSON multiple choice data.
        """
        data = json.loads(item)

        return cls(data["question"], data["answers"], **kwargs)

    @classmethod
    def from_xml(cls, item, **kwargs):
        """Create a ``MultipleChoice`` item from XML data.

        Create a ``MultipleChoice`` item from XML data.

        Parameters
        ----------
        cls
            The ``MultipleChoice`` class.
        item : str
            A string containing IMSCC multiple choice XML data.
        """
        tree = ET.fromstring(item)

        # Question text.
        q = tree.find("presentation").find("material").find("mattext").text

        # Correct answer.
        correct = (
            tree.find("resprocessing")
            .find("respcondition")
            .find("conditionvar")
            .find("varequal")
            .text
        )

        # Answer choices.
        a = [
            {
                "answer": ele.find("material").find("mattext").text,
                "correct": True if correct == ele.get("ident") else False,
            }
            for ele in (
                tree.find("presentation")
                .find("response_lid")
                .find("render_choice")
                .findall("response_label")
            )
        ]

        return cls(q, a, **kwargs)

    def to_json(self):
        """Create a multiple choice JSON string from item data."""
        # Correct answer.
        correct = (
            self.item.find("resprocessing")
            .find("respcondition")
            .find("conditionvar")
            .find("varequal")
            .text
        )

        return json.dumps(
            {
                "type": "multiple choice",
                "question": self.mattext.text,
                "answers": [
                    {
                        "answer": ele.find("material").find("mattext").text,
                        "correct": True if correct == ele.get("ident") else False,
                    }
                    for ele in self.choices.findall("response_label")
                ],
            }
        )

    def to_xml(self):
        """Create a multiple choice XML string from item data."""
        return ET.tostring(self.item, encoding="unicode")
