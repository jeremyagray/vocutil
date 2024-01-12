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

import defusedxml.ElementTree as ET


class Manifest:
    """A Common Cartridge manifest."""

    def __init__(self, **kwargs):
        """Initialize a manifest."""
        self.uuid = uuid.uuid4()
        self.manifest = ET.Element(
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
        self.metadata = ET.SubElement(self.manifest, "metadata")
        schema = ET.SubElement(self.metadata, "schema")
        schema.text = "IMS Common Cartridge"
        schemaversion = ET.SubElement(self.metadata, "schemaversion")
        schemaversion.text = "1.2.0"
        lom = ET.SubElement(self.metadata, "lomimscc:lom")
        general = ET.SubElement(lom, "lomimscc:general")
        title = ET.SubElement(general, "lomimscc:title")
        self.title = ET.SubElement(title, "lomimscc:string")
        if "title" in kwargs:
            self.title.text = str(kwargs["title"])

        # File and directory layout.
        self.organizations = ET.SubElement(self.manifest, "organizations")
        self.organization = ET.SubElement(
            self.organizations,
            "organization",
            identifier="org",
            structure="rooted-hierarchy",
        )
        self.root = ET.SubElement(self.organization, "item", identifier="root")

        # File locations.
        self.resources = ET.SubElement(self.manifest, "resources")

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
