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

"""Common Cartridge manifest."""

import xml.etree.ElementTree as ET


class Manifest:
    """A Common Cartridge manifest."""

    def __init__(self, **kwargs):
        """Initialize a manifest."""

        self.manifest = ET.Element(
            "manifest",
            attrib={
                "xmlns": "http://www.imsglobal.org/xsd/imsccv1p2/imscp_v1p1",
                "xmlns:lom": "http://ltsc.ieee.org/xsd/imsccv1p2/LOM/resource",
                "xmlns:lomimscc": "http://ltsc.ieee.org/xsd/imsccv1p2/LOM/manifest",
                "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "xsi:schemaLocation": "http://www.imsglobal.org/xsd/imsccv1p2/imscp_v1p1 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscp_v1p2_v1p0.xsd http://www.imsglobal.org/xsd/imsccv1p2/imsccauth_v1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imsccauth_v1p2.xsd http://ltsc.ieee.org/xsd/imsccv1p2/LOM/manifest http://www.imsglobal.org/profile/cc/ccv1p2/LOM/ccv1p2_lommanifest_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p2/LOM/resource http://www.imsglobal.org/profile/cc/ccv1p2/LOM/ccv1p2_lomresource_v1p0.xsd http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_qtiasiv1p2p1_v1p0.xsd http://www.imsglobal.org/xsd/imsccv1p2/imswl_v1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imswl_v1p2.xsd http://www.imsglobal.org/xsd/imsccv1p2/imsdt_v1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imsdt_v1p2.xsd http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscsmd_v1p0.xsd http://www.imsglobal.org/xsd/imslticc_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticc_v1p0p1.xsd http://www.imsglobal.org/xsd/imslticp_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticp_v1p0.xsd http://www.imsglobal.org/xsd/imslticm_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticm_v1p0.xsd http://www.imsglobal.org/xsd/imsbasiclti_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imsbasiclti_v1p0p1.xsd",
            },
        )
        self.manifest.set("identifier", str(kwargs["ident"]) if "ident" in kwargs else "manifest")

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
        self.organization = ET.SubElement(self.organizations, "organization", identifier="org", structure="rooted-hierarchy")
        self.root = ET.SubElement(self.organization, "item", identifier="root")

        # File locations.
        self.resources = ET.SubElement(self.manifest, "resources")

        return

    def set_ident(self, ident):
        """Set the ``ident`` field of the manifest."""
        if ident is not None:
            self.manifest.set("identifier", str(ident))

        return

    def set_title(self, title):
        """Set the ``title`` tag of the manifest."""
        if title is not None:
            self.title.text = str(title)

        return

    def append(self):
        """Append resources to the manifest."""
        # Add items to ``self.root`` in format:
        # <item identifier="id01" identifierref="cid01"><title>Chapter 15 Vocabulary FIB</title></item>
        # Tag:  item
        # Subtags:  title
        # Attributes:
        #   identifier:  unique identifier for the organizational item
        #   identifierref:  identifier of the associated resource

        # Add files to ``self.resources`` with correct type in format:
        # ``identifier`` is the unique identifier for the file and
        # Schoology uses it for the folder and file name as well.  The
        # type should be one of the following values:
        # <resource identifier="cid01" type="imsqti_xmlv1p2/imscc_xmlv1p2/question-bank"><metadata/><file href="cid01/cid01.xml"/></resource>
        # <resource identifier="ccres0000001" type="webcontent" href="ccres0000001/sound-and-light.pdf"><metadata/><file href="ccres0000001/sound-and-light.pdf"/></resource>
        # <resource identifier="ccres0000002" type="webcontent" href="ccres0000002/ccres0000002.html" intendeduse="assignment"><metadata/><file href="ccres0000002/ccres0000002.html"/></resource>
        # <resource identifier="ccres0000003" type="imsqti_xmlv1p2/imscc_xmlv1p2/assessment"><metadata/><file href="ccres0000003/ccres0000003.xml"/></resource>
