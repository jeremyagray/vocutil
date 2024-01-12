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

"""Common Cartridge item."""

import uuid


class Item:
    """A Common Cartridge item."""

    def __init__(self, **kwargs):
        """Initialize an item."""
        self.uuid = uuid.uuid4()

        return

    def __str__(self):
        """Stringify an item."""
        pass

    def __repr__(self):
        """Reproduce an item."""
        pass
