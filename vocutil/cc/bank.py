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

"""Common Cartridge question bank."""

import uuid
from xml.etree.ElementTree import Element as ETElement  # nosec B405
from xml.etree.ElementTree import SubElement as ETSubElement  # nosec B405


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
