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

"""Common Cartridge cartridge."""

import os
import uuid
import xml.etree.ElementTree as ET
import zipfile

from .manifest import Manifest


class Cartridge:
    """A Common Cartridge cartridge."""

    def __init__(self, title="default", **kwargs):
        """Initialize a cartridge."""
        self.uuid = uuid.uuid4()

        self.manifest = Manifest(title=str(title))

    def set_title(self, title):
        """Set the ``title`` tag of the cartridge/manifest."""
        if title is not None:
            self.manifest.title.text = str(title)

        return

    def _write(self, fh):
        """Write a cartridge zip archive contents."""
        # Create the resources directory.
        fh.mkdir("resources")
        # Create the manifest.
        fh.writestr(
            "imsmanifest.xml",
            ET.tostring(self.manifest.manifest, encoding="unicode", xml_declaration=True),
        )
        # Write the directory/files for each resource in the manifest.
        pass

    def write(self, filename="cartridge.imscc.zip", overwrite=False):
        """Write a cartridge zip archive."""
        try:
            with zipfile.ZipFile(filename, mode="x") as f:
                self._write(f)
        except FileExistsError:
            if overwrite:
                # Overwrite the existing file.
                with zipfile.ZipFile(filename, mode="w") as f:
                    self._write(f)
            else:
                # Refuse to overwrite an existing file.
                raise OSError(f"cowardly refusing to overwrite existing file {filename}")

        return
