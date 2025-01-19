.. ***************************************************************************
..
.. vocutil, educational vocabulary utilities.
..
.. Copyright 2022-2025 Jeremy A Gray <gray@flyquackswim.com>.
..
.. All rights reserved.
..
.. SPDX-License-Identifier: GPL-3.0-or-later
..
.. ***************************************************************************

=========
 vocutil
=========

Vocabulary utilities for educators and education platforms.

..
   .. image:: https://badge.fury.io/py/vocutil.svg
      :target: https://badge.fury.io/py/vocutil
      :alt: PyPI Version
   .. image:: https://readthedocs.org/projects/vocutil/badge/?version=latest
      :target: https://vocutil.readthedocs.io/en/latest/?badge=latest
      :alt: Documentation Status

Description
===========

This is a collection of utilities useful for generating and
manipulating materials for educational use.  Originally, the goal was
to automate creation of vocabulary quizzes, practice, and study
materials but has expanded significantly.

The most useful part of the code is the interface to
`Instructional Management System Common Cartridge (IMSCC) <https://www.imsglobal.org/cc/index.html>`_
instructional materials files (cartridges) which are used to export
and import data from and between learning management systems (LMS).
This interface can both read and write cartridges, allowing users to
create or customize their instructional content outside the usually
limited confines of the LMS.

Beware that assignments imported in IMSCC files are usually treated as
templates and only offer a subset of the features that the LMS offers
in its edited assignments.  For instance, Schoology (January 2024)
allows creation of fill-in-the-blank questions with multiple correct
answers but imports them from a cartridge file with only the first
correct answer.  Likewise, it supports multiple fill-in-the-blank
questions in its editor but cannot import them at all.

Despite these limitations, this is an excellent interface to create
programmatically generated assignments, question banks, notes, and
other resources that is missing from most LMSs.  With a small amount
of tooling, it is possible to create a workflow that builds a document
from its sources and includes the generated product in a cartridge and
subsequently updating the cartridge if the sources change (like
compiling from LaTeX to PDF and including the PDF in the cartridge).

Installation
============

Install vocutil with::

  pip install vocutil

or add as a poetry dependency.

Human-Friendly Data Formats
===========================

The XML used by IMSCC files is not friendly.  While it can be
human-readable, even simple fill-in-the-blank questions require a
tedious amount of XML boilerplate to comply with the format.
``vocutil`` reads and writes its information in human-friendly JSON by
default.

Glossary Data Format
--------------------

All glossary data is stored as JSON with the following format::

  {
    "course": {
      "title": string
    },
    "book": {
      "title": string,
      "author": string
    },
    "glossary": [
      {
        "word": string,
        "definition": string,
        "chapter": integer,
        "section": integer
      },
      ...
    ]
  }

Currently, only the ``"glossary"`` array and only the ``"word"`` and
``"definition"`` parts of each entry are used.

Fill-in-the-Blank Question Format
---------------------------------

All fill-in-the-blank question data is stored as JSON with the
following format::

  {
    "type": "fib",
    "question": "question text",
    "answers": [
      {
        "answer": "answer text",
        "case": "No"
      },
      ...
    ]
  }

Multiple answers are treated as correct variations.  ``"case"`` should
be ``"Yes"`` or ``"No"`` (default).  Each question should have at
least one answer.

Multiple Choice Question Format
-------------------------------

All multiple choice question data is stored as JSON with the following
format::

  {
    "type": "multiple choice",
    "question": "question text",
    "answers": [
      {
        "answer": "answer text",
        "correct": boolean
      },
      ...
    ]
  }

Answers are stored just multiple response types and the correct answer
should have ``"correct"`` be ``true``.  At most one answer can be
correct.

True/False Question Format
--------------------------

All true/false question data is stored as JSON with the following
format::

  {
    "type": "true/false",
    "question": "question text",
    "answers": boolean
  }

Multiple Response Question Format
---------------------------------

All multiple response question data is stored as JSON with the
following format::

  {
    "type": "multiple response",
    "question": "question text",
    "answers": [
      {
        "answer": "answer text",
        "correct": boolean
      },
      ...
    ]
  }

Answers are stored just multiple choice types, but all correct answers
should have ``"correct"`` be ``true``.  At least one answer should be
correct.

Copyright and License
=====================

SPDX-License-Identifier: `GPL-3.0-or-later <https://spdx.org/licenses/GPL-3.0-or-later.html>`_

vocutil, educational vocabulary utilities.

Copyright (C) 2022-2025 `Jeremy A Gray <gray@flyquackswim.com>`_.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Author
======

`Jeremy A Gray <gray@flyquackswim.com>`_
