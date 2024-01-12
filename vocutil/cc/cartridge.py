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

"""Common Cartridge cartridge."""

import io
import uuid
import zipfile

from .manifest import Manifest


class Cartridge:
    """A Common Cartridge cartridge."""

    def __init__(self, title="default", **kwargs):
        """Initialize a cartridge."""
        self.uuid = uuid.uuid4()

        self.manifest = Manifest(title=str(title))
        self.resources = []

    def set_title(self, title):
        """Set the ``title`` tag of the cartridge/manifest."""
        if title is not None:
            self.manifest.title.text = str(title)

        return

    def append(self, res):
        """Append a resource to the cartridge."""
        self.resources.append(res)
        self.manifest.append(res)

    def write(self, filename="cartridge.imscc.zip", overwrite=False):
        """Write a cartridge zip archive."""
        buf = io.BytesIO()

        with zipfile.ZipFile(buf, mode="x") as zip:
            zip.mkdir("resources")
            zip.writestr("imsmanifest.xml", str(self.manifest))

            for res in self.resources:
                zip.mkdir(str(res.resource_uuid))
                zip.writestr(res.resource_name, res.buffer)

        with open(filename, mode="wb") as f:
            f.write(buf.getvalue())

        return
