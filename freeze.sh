#!/bin/bash
#
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

grep='/usr/bin/grep'
pip='/home/gray/.virtualenvs/pccc/bin/pip'
sed='/usr/bin/sed'

pip freeze | ${sed} 's/ @ .*-\(.*\)\(-py[23]\|-cp39-cp39\|-cp36\|\.tar\).*$/==\1/' | ${grep} -v '\(poetry\|pccc\|pkg-resources\)'
