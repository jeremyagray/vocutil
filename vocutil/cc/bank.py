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

"""Common Cartridge question bank."""

import json
import uuid
from xml.etree.ElementTree import Element as ETElement  # nosec B405
from xml.etree.ElementTree import SubElement as ETSubElement  # nosec B405

import defusedxml.ElementTree as ET

from .utils import _load_json_item
from .utils import _load_xml_item


class Bank:
    """A Common Cartridge item bank."""

    def __init__(self, **kwargs):
        """Initialize an item bank."""
        self.uuid = uuid.uuid4()
        self.doc = ETElement(
            "questestinterop",
            attrib={
                "xmlns": "http://www.imsglobal.org/xsd/ims_qtiasiv1p2",
                "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "xsi:schemaLocation": "http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_qtiasiv1p2p1_v1p0.xsd",  # noqa: E501
            },
        )

        self.bank = ETSubElement(
            self.doc, "objectbank", attrib={"ident": str(self.uuid)}
        )

        return

    def append(self, item):
        """Append an item to the bank."""
        self.bank.append(item)

    @classmethod
    def from_json(cls, bank, **kwargs):
        """Create a ``Bank`` from JSON data.

        Create a ``Bank`` from JSON data.

        Parameters
        ----------
        cls
            The ``Bank`` class.
        bank : str
            A string containing JSON question bank data.
        """
        data = json.loads(bank)

        questions = cls(**kwargs)

        for item in data["questions"]:
            questions.bank.append(_load_json_item(item))

        return questions

    @classmethod
    def from_xml(cls, bank, **kwargs):
        """Create a ``Bank`` from XML data.

        Create a ``Bank`` from XML data.

        Parameters
        ----------
        cls
            The ``Bank`` class.
        item : str
            A string containing IMSCC item bank XML data.
        """
        tree = ET.fromstring(bank)
        questions = cls(**kwargs)

        if tree.find("objectbank") is not None:
            for item in tree.find("objectbank").findall("item"):
                questions.bank.append(_load_xml_item(item))

        return questions

    def to_json(self):
        """Create an item bank JSON string."""
        return json.dumps(
            {
                "type": "question bank",
                "questions": [json.loads(q) for q in self.bank.findall("item")],
            }
        )

    def to_xml(self, declaration=False):
        """Create an IMSCC item bank XML string."""
        return ET.tostring(
            self.doc,
            encoding="unicode",
            xml_declaration=declaration,
        )
