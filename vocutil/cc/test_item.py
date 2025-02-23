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

"""vocutil CC item tests."""

from uuid import UUID

import pytest

from vocutil.cc import Item


def test_item_should_have_valid_uuid():
    """``Item`` should have a valid UUID."""
    item = Item()
    assert str(UUID(str(item.uuid))) == str(item.uuid)


def test_from_dict_should_raise():
    """``Item.from_dict()`` should raise."""
    with pytest.raises(NotImplementedError):
        Item.from_dict({})


def test_from_json_should_raise():
    """``Item.from_json()`` should raise."""
    with pytest.raises(NotImplementedError):
        Item.from_json("")


def test_from_xml_should_raise():
    """``Item.from_xml()`` should raise."""
    with pytest.raises(NotImplementedError):
        Item.from_xml("")


def test_to_dict_should_raise():
    """``Item.to_dict()`` should raise."""
    with pytest.raises(NotImplementedError):
        item = Item()
        item.to_dict()


def test_to_json_should_raise():
    """``Item.to_json()`` should raise."""
    with pytest.raises(NotImplementedError):
        item = Item()
        item.to_json()


def test_to_xml_should_raise():
    """``Item.to_xml()`` should raise."""
    with pytest.raises(NotImplementedError):
        item = Item()
        item.to_xml()
