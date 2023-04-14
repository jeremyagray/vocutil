.. *****************************************************************************
..
.. vocutil, educational vocabulary utilities.
..
.. Copyright 2022-2023 Jeremy A Gray <gray@flyquackswim.com>.
..
.. All rights reserved.
..
.. SPDX-License-Identifier: GPL-3.0-or-later
..
.. *****************************************************************************

vocutil
=======

Vocabulary utilities for educators and education platforms.

..
   .. image:: https://badge.fury.io/py/vocutil.svg
      :target: https://badge.fury.io/py/vocutil
      :alt: PyPI Version
   .. image:: https://readthedocs.org/projects/vocutil/badge/?version=latest
      :target: https://vocutil.readthedocs.io/en/latest/?badge=latest
      :alt: Documentation Status

Description
-----------

This is a collection of utilities useful for generating and
manipulating vocabulary lists (words and definitions) for educational
use.

Installation
------------

Install vocutil with::

  pip install vocutil

or add as a poetry dependency.

If you desire a package locally built with poetry, download the
source, change the appropriate lines in ``pyproject.toml``, and
rebuild.

JSON Data Format
----------------

All glossary data is stored in a master JSON file with the following format:

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
      }
    ]
  }

Copyright and License
---------------------

SPDX-License-Identifier: `GPL-3.0-or-later <https://spdx.org/licenses/GPL-3.0-or-later.html>`_

vocutil, educational vocabulary utilities.

Copyright (C) 2022 `Jeremy A Gray <gray@flyquackswim.com>`_.

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
------

`Jeremy A Gray <gray@flyquackswim.com>`_
