# ******************************************************************************
#
# vocutil, educational vocabulary utilities.
#
# Copyright 2022 Jeremy A Gray <gray@flyquackswim.com>.
#
# All rights reserved.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# ******************************************************************************

"""Common Cartridge multiple choice item."""

import uuid
import xml.etree.ElementTree as ET


class MultipleChoice:
    """A Common Cartridge multiple choice item."""

    def __init__(self, qdata, **kwargs):
        """Initialize a multiple choice item."""
        self.uuid = uuid.uuid4()
        self.item = ET.Element("item", ident=str(self.uuid))
        self.itemmetadata = ET.SubElement(self.item, "itemmetadata")
        self.qtimetadata = ET.SubElement(self.itemmetadata, "qtimetadata")
        self.qtimetadatafield = ET.SubElement(self.qtimetadata, "qtimetadatafield")
        self.fieldlabel = ET.SubElement(self.qtimetadatafield, "fieldlabel")
        self.fieldlabel.text = "cc_profile"
        self.fieldentry = ET.SubElement(self.qtimetadatafield, "fieldentry")
        self.fieldentry.text = "cc.multiple_choice.v0p1"
        self.presentation = ET.SubElement(self.item, "presentation")
        self.material = ET.SubElement(self.presentation, "material")
        self.mattext = ET.SubElement(self.material, "mattext", texttype="text/html")
        self.mattext.text = qdata["question"]

        self.response = ET.SubElement(
            self.presentation,
            "response_lid",
            ident=str(self.uuid),
            rcardinality="Single",
        )
        self.choices = ET.SubElement(self.response, "render_choice")

        correct = None
        for i, ans in enumerate(qdata["answers"]):
            ident = f"{self.uuid}-{i}"
            choice = ET.SubElement(self.choices, "response_label", ident=ident)
            material = ET.SubElement(choice, "material")
            mattext = ET.SubElement(material, "mattext", texttype="text/plain")
            mattext.text = ans["answer"]
            if ans["correct"]:
                correct = ident

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
        varequal = ET.SubElement(condvar, "varequal", respident=str(self.uuid))
        varequal.text = correct
        setvar = ET.SubElement(cond, "setvar", action="Set", varname="SCORE")
        setvar.text = "100"

        return
