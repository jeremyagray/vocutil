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

"""Common Cartridge assessment."""

import xml.etree.ElementTree as ET


class Assessment:
    """A Common Cartridge assessment."""

    def __init__(self, **kwargs):
        """Initialize an assessment."""
        self.doc = ET.Element(
            "questestinterop",
            attrib={
                "xmlns": "http://www.imsglobal.org/xsd/ims_qtiasiv1p2",
                "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "xsi:schemaLocation": "http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_qtiasiv1p2p1_v1p0.xsd",
            },
        )
        self.assessment = ET.SubElement(self.doc, "assessment")
        self.assessment.set("ident", str(kwargs["ident"])) if "ident" in kwargs else ""
        self.assessment.set("title", str(kwargs["title"])) if "title" in kwargs else ""
        self.qtimetadata = ET.SubElement(self.assessment, "qtimetadata")

        metadata = (
            ("cc_profile", "cc.exam.v0p1"),
            ("qmd_assessmenttype", "Examination"),
            ("qmd_scoretype", "Percentage"),
            ("cc_maxattempts", kwargs["attempts"] if "attempts" in kwargs else "1"),
        )

        for datum in metadata:
            qtimetadatafield = ET.SubElement(self.qtimetadata, "qtimetadatafield")
            fieldlabel = ET.SubElement(qtimetadatafield, "fieldlabel")
            fieldlabel.text = datum[0]
            fieldentry = ET.SubElement(qtimetadatafield, "fieldentry")
            fieldentry.text = datum[1]

        self.presentation_material = ET.SubElement(
            self.assessment, "presentation_material"
        )
        flow_mat = ET.SubElement(self.presentation_material, "flow_mat")
        material = ET.SubElement(flow_mat, "material")
        self.instructions = ET.SubElement(
            material,
            "mattext",
            attrib={
                "texttype": "text/html",
            },
        )

        if "instructions" in kwargs:
            self.instructions.text = str(kwargs["instructions"])

        self.section = ET.SubElement(self.assessment, "section", ident="root_section")

        return

    def set_ident(self, ident):
        """Set the ``ident`` field of the assessment."""
        if ident is not None:
            self.assessment.set("ident", str(ident))

    def set_title(self, title):
        """Set the ``title`` field of the assessment."""
        if title is not None:
            self.assessment.set("title", str(title))

    def set_attempts(self, attempts):
        """Set the allowed number of attempts."""
        if attempts is not None:
            for field in self.qtimetadata.findall("qtimetadatafield"):
                if field.find("fieldentry").text == "cc_maxattempts":
                    field.find("fieldlabel").text == attempts
                    break
