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

"""Common Cartridge fill-in-the-blank item."""

import xml.etree.ElementTree as ET

from .item import Item


class FillInTheBlank(Item):
    """A Common Cartridge fill in the blank item."""

    def __init__(self, question, answers, case="No", **kwargs):
        """Initialize a fill in the item."""
        super().__init__(**kwargs)
        self.question = question
        self.answers = answers
        self.case = case if case == "Yes" else "No"

        self.item = ET.Element("item", ident=str(self.uuid))
        self.itemmetadata = ET.SubElement(self.item, "itemmetadata")
        self.qtimetadata = ET.SubElement(self.itemmetadata, "qtimetadata")
        self.qtimetadatafield = ET.SubElement(self.qtimetadata, "qtimetadatafield")
        self.fieldlabel = ET.SubElement(self.qtimetadatafield, "fieldlabel")
        self.fieldlabel.text = "cc_profile"
        self.fieldentry = ET.SubElement(self.qtimetadatafield, "fieldentry")
        self.fieldentry.text = "cc.fib.v0p1"
        self.presentation = ET.SubElement(self.item, "presentation")
        self.material = ET.SubElement(self.presentation, "material")
        self.mattext = ET.SubElement(self.material, "mattext", texttype="text/html")
        self.mattext.text = self.question

        self.response = ET.SubElement(
            self.presentation,
            "response_str",
            rcardinality="Single",
            ident=f"fib-resp-{str(self.uuid)}",
        )
        self.blank = ET.SubElement(self.response, "render_fib", prompt="Dashline")

        grade = ET.SubElement(self.item, "resprocessing")
        outcomes = ET.SubElement(grade, "outcomes")
        decvar = ET.SubElement(
            outcomes,
            "decvar",
            maxvalue="100",
            minvalue="0",
            varname="SCORE",
            vartype="Decimal",
        )
        cond = ET.SubElement(
            grade,
            "respcondition",
            attrib={
                "continue": "No",
            },
        )
        condvar = ET.SubElement(cond, "conditionvar")

        # Set possible correct answers.
        for answer in self.answers:
            varequal = ET.SubElement(
                condvar,
                "varequal",
                case=self.case,
                respident=f"fib-resp-{str(self.uuid)}",
            )
            varequal.text = answer

        setvar = ET.SubElement(cond, "setvar", action="Set", varname="SCORE")
        setvar.text = "100"

        return

    def to_xml(self):
        """Initialize a fill in the item."""
        item = ET.Element("item", ident=str(self.uuid))
        itemmetadata = ET.SubElement(item, "itemmetadata")
        qtimetadata = ET.SubElement(itemmetadata, "qtimetadata")
        qtimetadatafield = ET.SubElement(qtimetadata, "qtimetadatafield")
        fieldlabel = ET.SubElement(qtimetadatafield, "fieldlabel")
        fieldlabel.text = "cc_profile"
        fieldentry = ET.SubElement(qtimetadatafield, "fieldentry")
        fieldentry.text = "cc.fib.v0p1"
        presentation = ET.SubElement(item, "presentation")
        material = ET.SubElement(presentation, "material")
        mattext = ET.SubElement(material, "mattext", texttype="text/html")
        mattext.text = self.question

        response = ET.SubElement(
            presentation,
            "response_str",
            rcardinality="Single",
            ident=f"fib-resp-{str(self.uuid)}",
        )
        blank = ET.SubElement(response, "render_fib", prompt="Dashline")

        grade = ET.SubElement(item, "resprocessing")
        outcomes = ET.SubElement(grade, "outcomes")
        decvar = ET.SubElement(
            outcomes,
            "decvar",
            maxvalue="100",
            minvalue="0",
            varname="SCORE",
            vartype="Decimal",
        )
        cond = ET.SubElement(
            grade,
            "respcondition",
            attrib={
                "continue": "No",
            },
        )
        condvar = ET.SubElement(cond, "conditionvar")

        # Set possible correct answers.
        for answer in self.answers:
            varequal = ET.SubElement(
                condvar,
                "varequal",
                case=self.case,
                respident=f"fib-resp-{str(self.uuid)}",
            )
            varequal.text = answer

        setvar = ET.SubElement(cond, "setvar", action="Set", varname="SCORE")
        setvar.text = "100"

        return ET.tostring(item, encoding="unicode")
