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

"""Common Cartridge multiple choice item."""

import uuid
from xml.etree.ElementTree import Element as ETElement  # nosec B405
from xml.etree.ElementTree import SubElement as ETSubElement  # nosec B405


class MultipleChoice:
    """A Common Cartridge multiple choice item."""

    def __init__(self, qdata, **kwargs):
        """Initialize a multiple choice item."""
        self.uuid = uuid.uuid4()
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
        self.mattext.text = qdata["question"]

        self.response = ETSubElement(
            self.presentation,
            "response_lid",
            ident=str(self.uuid),
            rcardinality="Single",
        )
        self.choices = ETSubElement(self.response, "render_choice")

        correct = None
        for i, ans in enumerate(qdata["answers"]):
            ident = f"{self.uuid}-{i}"
            choice = ETSubElement(self.choices, "response_label", ident=ident)
            material = ETSubElement(choice, "material")
            mattext = ETSubElement(material, "mattext", texttype="text/plain")
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
