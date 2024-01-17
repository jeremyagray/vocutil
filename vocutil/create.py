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

"""Create the boilerplate for a new unit."""

import os
import sys
from pathlib import Path

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import TemplateNotFound


def _maybe_write_file_from_template(template, path, data, latex=False):
    """Write a file if it does not exist."""
    if latex:
        jinja = Environment(
            loader=FileSystemLoader("templates"),
            block_start_string=r"\BLOCK{",
            block_end_string="}",
            variable_start_string=r"\VAR{",
            variable_end_string="}",
            comment_start_string=r"\#{",
            comment_end_string="}",
            line_statement_prefix="%%",
            line_comment_prefix="%#",
            trim_blocks=True,
            autoescape=True,
            keep_trailing_newline=True,
        )
    else:
        jinja = Environment(
            loader=FileSystemLoader("templates"),
            trim_blocks=True,
            autoescape=True,
            keep_trailing_newline=True,
        )

    try:
        template = jinja.get_template(template)
    except TemplateNotFound:
        print(f"no template found for file {str(path)}, skipping...")
        return

    try:
        with open(path, "x") as f:
            f.write(template.render(data))
    except FileExistsError:
        print(f"boilerplate file {str(path)} exists, skipping...")
        pass


def maybe_create_directories(dest, unit, prefix):  # dead: disable
    """Create directories for the unit as necessary."""
    dirs = [
        dest,
        dest / "sources",
        dest / "sources" / "unused",
        dest / "sources" / "used",
    ]

    for dir in dirs:
        try:
            os.makedirs(dir)
        except FileExistsError:
            print(f"boilerplate directory {dir} exists, skipping...")
        except OSError:
            print(f"problem creating boilerplate directory {dir}")
            sys.exit(1)


def maybe_create_makefile(dest, unit, prefix):
    """Create a makefile for the unit if necessary."""
    _maybe_write_file_from_template(
        "Makefile", dest / "Makefile", {"unit": unit, "prefix": prefix}, latex=False
    )


def maybe_create_cartridge_generator(dest, unit, prefix):
    """Create a cartridge generator for the unit if necessary."""
    _maybe_write_file_from_template(
        "cartridge.py",
        dest / f"{prefix}-cartridge.py",
        {
            "unit": unit,
            "prefix": prefix,
            "chapter": str(dest).split("-")[0].lstrip("0"),
        },
        latex=False,
    )


def maybe_create_notes(dest, unit, prefix):
    """Create an empty notes presentation for the unit if necessary."""
    _maybe_write_file_from_template(
        "slides.tex",
        dest / f"{prefix}-slides.tex",
        {"unit": unit, "prefix": prefix},
        latex=True,
    )


def maybe_create_bibliographic_database(dest, unit, prefix):
    """Create a bibliographic database if necessary."""
    _maybe_write_file_from_template(
        "slides.bib",
        dest / f"{prefix}.bib",
        {"unit": unit, "prefix": prefix},
        latex=False,
    )


def maybe_create_glossary(dest, unit, prefix):
    """Create an empty glossary if necessary."""
    _maybe_write_file_from_template(
        "glossary.json",
        dest / "glossary.json",
        {"unit": unit, "prefix": prefix},
        latex=False,
    )
    _maybe_write_file_from_template(
        "cumulative.json",
        dest / "cumulative.json",
        {"unit": unit, "prefix": prefix},
        latex=False,
    )


def create_unit():
    """Orchestrate creation of the boilerplate for a new unit."""
    try:
        dest = Path(sys.argv[1])
    except IndexError:
        print("provide a unit directory", file=sys.stderr)
        sys.exit(1)

    try:
        unit = sys.argv[2]
    except IndexError:
        print("provide a unit name", file=sys.stderr)
        sys.exit(1)

    try:
        prefix = sys.argv[3]
    except IndexError:
        print("provide a unit prefix", file=sys.stderr)
        sys.exit(1)

    maybe_create_directories(dest, unit, prefix)
    maybe_create_makefile(dest, unit, prefix)
    maybe_create_notes(dest, unit, prefix)
    maybe_create_cartridge_generator(dest, unit, prefix)
    maybe_create_bibliographic_database(dest, unit, prefix)
    maybe_create_glossary(dest, unit, prefix)
