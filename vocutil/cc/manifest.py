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

"""Common Cartridge manifest."""

import uuid
from xml.etree.ElementTree import Element as ETElement  # nosec B405
from xml.etree.ElementTree import SubElement as ETSubElement  # nosec B405

import defusedxml.ElementTree as ET


class Manifest:
    """A Common Cartridge manifest."""

    def __init__(self, **kwargs):
        """Initialize a manifest."""
        self.uuid = uuid.uuid4()
        self.manifest = ETElement(
            "manifest",
            attrib={
                "xmlns": "http://www.imsglobal.org/xsd/imsccv1p2/imscp_v1p1",
                "xmlns:lom": "http://ltsc.ieee.org/xsd/imsccv1p2/LOM/resource",
                "xmlns:lomimscc": "http://ltsc.ieee.org/xsd/imsccv1p2/LOM/manifest",
                "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "xsi:schemaLocation": "http://www.imsglobal.org/xsd/imsccv1p2/imscp_v1p1 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscp_v1p2_v1p0.xsd http://www.imsglobal.org/xsd/imsccv1p2/imsccauth_v1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imsccauth_v1p2.xsd http://ltsc.ieee.org/xsd/imsccv1p2/LOM/manifest http://www.imsglobal.org/profile/cc/ccv1p2/LOM/ccv1p2_lommanifest_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p2/LOM/resource http://www.imsglobal.org/profile/cc/ccv1p2/LOM/ccv1p2_lomresource_v1p0.xsd http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_qtiasiv1p2p1_v1p0.xsd http://www.imsglobal.org/xsd/imsccv1p2/imswl_v1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imswl_v1p2.xsd http://www.imsglobal.org/xsd/imsccv1p2/imsdt_v1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imsdt_v1p2.xsd http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscsmd_v1p0.xsd http://www.imsglobal.org/xsd/imslticc_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticc_v1p0p1.xsd http://www.imsglobal.org/xsd/imslticp_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticp_v1p0.xsd http://www.imsglobal.org/xsd/imslticm_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticm_v1p0.xsd http://www.imsglobal.org/xsd/imsbasiclti_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imsbasiclti_v1p0p1.xsd",  # noqa: E501
                "identifier": str(self.uuid),
            },
        )

        # Cartridge metadata.
        self.metadata = ETSubElement(self.manifest, "metadata")
        schema = ETSubElement(self.metadata, "schema")
        schema.text = "IMS Common Cartridge"
        schemaversion = ETSubElement(self.metadata, "schemaversion")
        schemaversion.text = "1.2.0"
        lom = ETSubElement(self.metadata, "lomimscc:lom")
        general = ETSubElement(lom, "lomimscc:general")
        title = ETSubElement(general, "lomimscc:title")
        self.title = ETSubElement(title, "lomimscc:string")
        if "title" in kwargs:
            self.title.text = str(kwargs["title"])

        # File and directory layout.
        self.organizations = ETSubElement(self.manifest, "organizations")
        self.organization = ETSubElement(
            self.organizations,
            "organization",
            identifier="org",
            structure="rooted-hierarchy",
        )
        self.root = ETSubElement(self.organization, "item", identifier="root")

        # File locations.
        self.resources = ETSubElement(self.manifest, "resources")

        return

    def __str__(self):
        """Stringify myself."""
        return ET.tostring(self.manifest, encoding="unicode", xml_declaration=True)

    def set_title(self, title):
        """Set the ``title`` tag of the manifest."""
        if title is not None:
            self.title.text = str(title)

        return

    def append(self, res):
        """Append resources to the manifest."""
        self.root.append(res.item)
        self.resources.append(res.resource)
