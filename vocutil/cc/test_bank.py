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

"""vocutil CC item bank tests."""

import json

import vocutil


def test_should_create_empty_bank():
    """Should create an empty bank."""
    questions = vocutil.cc.Bank()

    expected = f"""<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_qtiasiv1p2p1_v1p0.xsd"><objectbank ident="{str(questions.uuid)}" /></questestinterop>"""  # noqa: E501

    actual = questions.to_xml()

    assert actual == expected


def test_should_create_empty_bank_from_json():
    """Should create an empty bank from JSON."""
    questions = vocutil.cc.Bank.from_json(
        json.dumps(
            {
                "type": "question bank",
                "questions": [],
            }
        )
    )

    expected = f"""<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_qtiasiv1p2p1_v1p0.xsd"><objectbank ident="{str(questions.uuid)}" /></questestinterop>"""  # noqa: E501

    actual = questions.to_xml()

    assert actual == expected


def test_should_create_empty_bank_from_xml():
    """Should create an empty bank from IMSCC question bank XML."""
    bank = """<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_qtiasiv1p2p1_v1p0.xsd"><objectbank ident="1" /></questestinterop>"""  # noqa: E501

    questions = vocutil.cc.Bank.from_xml(bank)

    expected = f"""<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_qtiasiv1p2p1_v1p0.xsd"><objectbank ident="{str(questions.uuid)}" /></questestinterop>"""  # noqa: E501

    actual = questions.to_xml()

    assert actual == expected


def test_should_export_empty_json_bank():
    """Should export an empty JSON bank."""
    questions = vocutil.cc.Bank.from_json(
        json.dumps(
            {
                "type": "question bank",
                "questions": [],
            }
        )
    )

    expected = {
        "type": "question bank",
        "questions": [],
    }

    actual = json.loads(questions.to_json())

    assert actual == expected
