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

"""Common Cartridge true/false item."""

import json
from xml.etree.ElementTree import Element as ETElement  # nosec B405
from xml.etree.ElementTree import SubElement as ETSubElement  # nosec B405

import defusedxml.ElementTree as ET

from .item import Item


class TrueFalse(Item):
    """A Common Cartridge true/false item."""

    def __init__(self, question, answer, **kwargs):
        """Initialize a ``TrueFalse`` item.

        Initialize a ``TrueFalse`` item.

        Parameters
        ----------
        question : str
            The HTML formatted question text.
        answer : bool
            The Boolean answer.
        """
        # Call the super.
        super().__init__(**kwargs)

        self.question = question
        self.answer = answer

        self.item = ETElement("item", ident=str(self.uuid))
        self.itemmetadata = ETSubElement(self.item, "itemmetadata")
        self.qtimetadata = ETSubElement(self.itemmetadata, "qtimetadata")
        self.qtimetadatafield = ETSubElement(self.qtimetadata, "qtimetadatafield")
        self.fieldlabel = ETSubElement(self.qtimetadatafield, "fieldlabel")
        self.fieldlabel.text = "cc_profile"
        self.fieldentry = ETSubElement(self.qtimetadatafield, "fieldentry")
        self.fieldentry.text = "cc.true_false.v0p1"
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

        correct = f"{self.uuid}-01" if answer else f"{self.uuid}-02"

        # True.
        ident = f"{self.uuid}-01"
        choice = ETSubElement(self.choices, "response_label", ident=ident)
        material = ETSubElement(choice, "material")
        mattext = ETSubElement(material, "mattext", texttype="text/plain")
        mattext.text = "True"

        # False.
        ident = f"{self.uuid}-02"
        choice = ETSubElement(self.choices, "response_label", ident=ident)
        material = ETSubElement(choice, "material")
        mattext = ETSubElement(material, "mattext", texttype="text/plain")
        mattext.text = "False"

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
        """Create a ``TrueFalse`` item from JSON data.

        Create a ``TrueFalse`` item from JSON data.

        Parameters
        ----------
        cls
            The ``TrueFalse`` class.
        item : str
            A string containing true/false JSON data.
        """
        data = json.loads(item)

        return cls(data["question"], data["answer"], **kwargs)

    @classmethod
    def from_xml(cls, item, **kwargs):
        """Create a ``TrueFalse`` item from XML data.

        Create a ``TrueFalse`` item from XML data.

        Parameters
        ----------
        cls
            The ``TrueFalse`` class.
        item : str
            A string containing IMSCC true/false XML data.
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
        a = None
        for ele in (
            tree.find("presentation")
            .find("response_lid")
            .find("render_choice")
            .findall("response_label")
        ):
            if correct == ele.get("ident"):
                a = (
                    True
                    if ele.find("material").find("mattext").text.lower() == "true"
                    else False
                )
                break

        return cls(q, a, **kwargs)

    def to_json(self):
        """Create a true/false JSON string from item data."""
        # Correct answer.
        correct = (
            self.item.find("resprocessing")
            .find("respcondition")
            .find("conditionvar")
            .find("varequal")
            .text
        )

        for ele in self.choices.findall("response_label"):
            if correct == ele.get("ident"):
                answer = (
                    True
                    if ele.find("material").find("mattext").text.lower() == "true"
                    else False
                )

        return json.dumps(
            {
                "type": "true/false",
                "question": str(
                    self.item.find("presentation").find("material").find("mattext").text
                ),
                "answer": answer,
            }
        )

    def to_xml(self, declaration=False):
        """Create a true/false XML string from item data."""
        return ET.tostring(
            self.item,
            encoding="unicode",
            xml_declaration=declaration,
        )
