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

"""vocutil CC item bank tests."""

import sys

import defusedxml.ElementTree as ET

# import pytest

sys.path.insert(0, "/home/gray/src/work/vocutil")

import vocutil  # noqa: E402


def test_empty_manifest():
    """Should produce an empty manifest."""
    manifest = vocutil.cc.Manifest(
        title="Chapter 15:  Sound and Light",
    )

    actual = f"""<manifest xmlns="http://www.imsglobal.org/xsd/imsccv1p2/imscp_v1p1" xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p2/LOM/resource" xmlns:lomimscc="http://ltsc.ieee.org/xsd/imsccv1p2/LOM/manifest" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p2/imscp_v1p1 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscp_v1p2_v1p0.xsd http://www.imsglobal.org/xsd/imsccv1p2/imsccauth_v1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imsccauth_v1p2.xsd http://ltsc.ieee.org/xsd/imsccv1p2/LOM/manifest http://www.imsglobal.org/profile/cc/ccv1p2/LOM/ccv1p2_lommanifest_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p2/LOM/resource http://www.imsglobal.org/profile/cc/ccv1p2/LOM/ccv1p2_lomresource_v1p0.xsd http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_qtiasiv1p2p1_v1p0.xsd http://www.imsglobal.org/xsd/imsccv1p2/imswl_v1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imswl_v1p2.xsd http://www.imsglobal.org/xsd/imsccv1p2/imsdt_v1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imsdt_v1p2.xsd http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscsmd_v1p0.xsd http://www.imsglobal.org/xsd/imslticc_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticc_v1p0p1.xsd http://www.imsglobal.org/xsd/imslticp_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticp_v1p0.xsd http://www.imsglobal.org/xsd/imslticm_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticm_v1p0.xsd http://www.imsglobal.org/xsd/imsbasiclti_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imsbasiclti_v1p0p1.xsd" identifier="{str(manifest.uuid)}"><metadata><schema>IMS Common Cartridge</schema><schemaversion>1.2.0</schemaversion><lomimscc:lom><lomimscc:general><lomimscc:title><lomimscc:string>Chapter 15:  Sound and Light</lomimscc:string></lomimscc:title></lomimscc:general></lomimscc:lom></metadata><organizations><organization identifier="org" structure="rooted-hierarchy"><item identifier="root" /></organization></organizations><resources /></manifest>"""  # noqa: E501

    expected = ET.tostring(
        manifest.manifest,
        encoding="unicode",
    )

    assert actual == expected


def test_set_title():
    """Should set the manifest title."""
    manifest = vocutil.cc.Manifest(
        title="test",
    )
    manifest.set_title("Chapter 15:  Sound and Light")

    actual = f"""<manifest xmlns="http://www.imsglobal.org/xsd/imsccv1p2/imscp_v1p1" xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p2/LOM/resource" xmlns:lomimscc="http://ltsc.ieee.org/xsd/imsccv1p2/LOM/manifest" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p2/imscp_v1p1 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscp_v1p2_v1p0.xsd http://www.imsglobal.org/xsd/imsccv1p2/imsccauth_v1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imsccauth_v1p2.xsd http://ltsc.ieee.org/xsd/imsccv1p2/LOM/manifest http://www.imsglobal.org/profile/cc/ccv1p2/LOM/ccv1p2_lommanifest_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p2/LOM/resource http://www.imsglobal.org/profile/cc/ccv1p2/LOM/ccv1p2_lomresource_v1p0.xsd http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_qtiasiv1p2p1_v1p0.xsd http://www.imsglobal.org/xsd/imsccv1p2/imswl_v1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imswl_v1p2.xsd http://www.imsglobal.org/xsd/imsccv1p2/imsdt_v1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imsdt_v1p2.xsd http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscsmd_v1p0.xsd http://www.imsglobal.org/xsd/imslticc_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticc_v1p0p1.xsd http://www.imsglobal.org/xsd/imslticp_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticp_v1p0.xsd http://www.imsglobal.org/xsd/imslticm_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticm_v1p0.xsd http://www.imsglobal.org/xsd/imsbasiclti_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imsbasiclti_v1p0p1.xsd" identifier="{str(manifest.uuid)}"><metadata><schema>IMS Common Cartridge</schema><schemaversion>1.2.0</schemaversion><lomimscc:lom><lomimscc:general><lomimscc:title><lomimscc:string>Chapter 15:  Sound and Light</lomimscc:string></lomimscc:title></lomimscc:general></lomimscc:lom></metadata><organizations><organization identifier="org" structure="rooted-hierarchy"><item identifier="root" /></organization></organizations><resources /></manifest>"""  # noqa: E501

    expected = ET.tostring(
        manifest.manifest,
        encoding="unicode",
    )

    assert actual == expected
