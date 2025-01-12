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

"""Common Cartridge item."""

import uuid


class Item:
    """A Common Cartridge question item.

    A general Common Cartridge question item.  All other question
    types are subclassed from ``Item``.
    """

    def __init__(self, **kwargs):
        """Initialize an item."""
        self.uuid = uuid.uuid4()

        return

    @classmethod
    def from_json(cls, data, **kwargs):
        """Instantiate from JSON data.

        Instantiate from JSON data.  Subclasses should override this
        method.

        Parameters
        ----------
        cls
            The ``Item`` class.
        data : str
            A string containing JSON data with which to generate the
            item.

        Raises
        ------
        NotImplementedError
            Raises if you do not implement this part of the interface
            you filthy animal.
        """
        raise NotImplementedError(
            "Items inheriting from ``Item`` should implement their own"
            " ``from_json()`` interface."
        )

    @classmethod
    def from_xml(cls, item, **kwargs):
        """Instantiate from IMSCC XML data.

        Instantiate from IMSCC XML data.  Subclasses should override
        this method.

        Parameters
        ----------
        cls
            The ``Item`` class.
        item : str
            A string containing IMSCC multiple choice XML data with
            which to generate the item.

        Raises
        ------
        NotImplementedError
            Raises if you do not implement this part of the interface
            you filthy animal.
        """
        raise NotImplementedError(
            "Items inheriting from ``Item`` should implement"
            " their own ``from_xml()`` interface."
        )

    def to_json(self):
        """Create a string of JSON item data.

        Create a string of JSON item data.  Subclasses should override
        this method.

        Raises
        ------
        NotImplementedError
            Raises if you do not implement this part of the interface
            you filthy animal.
        """
        raise NotImplementedError(
            "Items inheriting from ``Item`` should implement"
            " their own ``to_json()`` interface."
        )

    def to_xml(self):
        """Create a string of IMSCC XML data.

        Create a string of IMSCC XML data.  Subclasses should override
        this method.

        Raises
        ------
        NotImplementedError
            Raises if you do not implement this part of the interface
            you filthy animal.
        """
        raise NotImplementedError(
            "Items inheriting from ``Item`` should implement"
            " their own ``to_xml()`` interface."
        )
