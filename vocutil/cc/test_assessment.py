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

"""vocutil CC assessment tests."""

import sys
import xml.etree.ElementTree as ET

# import pytest

sys.path.insert(0, "/home/gray/src/work/vocutil")

import vocutil  # noqa: E402


def test_correct_xml():
    """Should produce correct XML."""
    actual = """<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_qtiasiv1p2p1_v1p0.xsd"><assessment ident="cid01" title="Section 15.3 Quiz"><qtimetadata><qtimetadatafield><fieldlabel>cc_profile</fieldlabel><fieldentry>cc.exam.v0p1</fieldentry></qtimetadatafield><qtimetadatafield><fieldlabel>qmd_assessmenttype</fieldlabel><fieldentry>Examination</fieldentry></qtimetadatafield><qtimetadatafield><fieldlabel>qmd_scoretype</fieldlabel><fieldentry>Percentage</fieldentry></qtimetadatafield><qtimetadatafield><fieldlabel>cc_maxattempts</fieldlabel><fieldentry>unlimited</fieldentry></qtimetadatafield></qtimetadata><presentation_material><flow_mat><material><mattext texttype="TEXT/HTML">&lt;p&gt;Answer the following questions about mirrors and color theory from section 15.3.&lt;/p&gt;</mattext></material></flow_mat></presentation_material><section ident="root_section" /></assessment></questestinterop>"""
    expected = ET.tostring(vocutil.cc.Assessment(
        ident="cid01",
        title="Section 15.3 Quiz",
        instructions="<p>Answer the following questions about mirrors and color theory from section 15.3.</p>",
        attempts="unlimited",
    ).doc, encoding="unicode")

    assert actual == expected
