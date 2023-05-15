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

"""vocutil CC item bank tests."""

import sys
import xml.etree.ElementTree as ET

# import pytest

sys.path.insert(0, "/home/gray/src/work/vocutil")

import vocutil  # noqa: E402


def test_empty_item_bank():
    """Should produce an empty item bank."""
    actual = """<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_qtiasiv1p2p1_v1p0.xsd"><objectbank ident="cid01" /></questestinterop>"""
    expected = ET.tostring(
        vocutil.cc.Bank(
            ident="cid01",
        ).doc,
        encoding="unicode",
    )

    assert actual == expected


def test_empty_item_bank_no_ident():
    """Should produce an empty item bank."""
    actual = """<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_qtiasiv1p2p1_v1p0.xsd"><objectbank ident="" /></questestinterop>"""
    expected = ET.tostring(
        vocutil.cc.Bank().doc,
        encoding="unicode",
    )

    assert actual == expected


def test_set_bank_ident():
    """Should set the ident of an item bank."""
    actual = """<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_qtiasiv1p2p1_v1p0.xsd"><objectbank ident="cid02" /></questestinterop>"""

    bank = vocutil.cc.Bank()
    bank.set_ident("cid02")

    expected = ET.tostring(
        bank.doc,
        encoding="unicode",
    )

    assert actual == expected
