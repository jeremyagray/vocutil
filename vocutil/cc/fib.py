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

"""Common Cartridge fill-in-the-blank item."""

from xml.etree.ElementTree import Element as ETElement  # nosec B405
from xml.etree.ElementTree import SubElement as ETSubElement  # nosec B405

import defusedxml.ElementTree as ET

from .item import Item


class FillInTheBlank(Item):
    """A Common Cartridge fill in the blank item."""

    def __init__(self, question, answers, case="No", **kwargs):
        """Initialize a fill in the item."""
        super().__init__(**kwargs)
        self.question = question
        self.answers = answers
        self.case = case if case == "Yes" else "No"

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
                case=self.case,
                respident=f"fib-resp-{str(self.uuid)}",
            )
            varequal.text = answer

        setvar = ETSubElement(cond, "setvar", action="Set", varname="SCORE")
        setvar.text = "100"

        return

    def to_xml(self):
        """Initialize a fill in the blank item."""
        item = ETElement("item", ident=str(self.uuid))
        itemmetadata = ETSubElement(item, "itemmetadata")
        qtimetadata = ETSubElement(itemmetadata, "qtimetadata")
        qtimetadatafield = ETSubElement(qtimetadata, "qtimetadatafield")
        fieldlabel = ETSubElement(qtimetadatafield, "fieldlabel")
        fieldlabel.text = "cc_profile"
        fieldentry = ETSubElement(qtimetadatafield, "fieldentry")
        fieldentry.text = "cc.fib.v0p1"
        presentation = ETSubElement(item, "presentation")
        material = ETSubElement(presentation, "material")
        mattext = ETSubElement(material, "mattext", texttype="text/html")
        mattext.text = self.question

        response = ETSubElement(
            presentation,
            "response_str",
            rcardinality="Single",
            ident=f"fib-resp-{str(self.uuid)}",
        )
        ETSubElement(response, "render_fib", prompt="Dashline")

        grade = ETSubElement(item, "resprocessing")
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
                case=self.case,
                respident=f"fib-resp-{str(self.uuid)}",
            )
            varequal.text = answer

        setvar = ETSubElement(cond, "setvar", action="Set", varname="SCORE")
        setvar.text = "100"

        return ET.tostring(item, encoding="unicode")
