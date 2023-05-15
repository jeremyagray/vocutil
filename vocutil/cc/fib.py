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


class FillInTheBlank:
    """A Common Cartridge fill in the blank item."""

    def __init__(self, qdata, **kwargs):
        """Initialize a fill in the item."""
        self.item = ET.Element("item", ident=str(kwargs["ident"]))
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
        self.mattext.text = qdata["question"]

        self.response = ET.SubElement(
            self.presentation,
            "response_str",
            rcardinality="Single",
            ident=f"fib-resp-{kwargs['ident']}",
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
        for answer in qdata["answers"]:
            varequal = ET.SubElement(
                condvar,
                "varequal",
                case=qdata["case"] if qdata["case"] == "Yes" else "No",
                respident=f"fib-resp-{kwargs['ident']}",
            )
            varequal.text = answer

        setvar = ET.SubElement(cond, "setvar", action="Set", varname="SCORE")
        setvar.text = "100"

        return
