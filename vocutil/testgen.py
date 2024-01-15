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

"""Parse Pearson TestGen questions."""

import pyparsing as pp
from docx import Document
from docx.opc.exceptions import PackageNotFoundError

PYPARSING_DEBUG = False


def _load_testgen_file(fn):
    """Load a Pearson TestGen file.

    Load a Pearson TestGen file in either Microsoft Word DOCX or text
    format, returning the document text for parsing.

    Parameters
    ----------
    fn : str
        The TestGen filename containing the text to be parsed.

    Returns
    -------
    str
        The text contained in the file.

    Raises
    ------
    FileNotFoundError
        Raised on a non-existent file from underlying code.
    """
    try:
        # Hopefully MS DOCX format.
        doc = Document(fn)
        text = "\n".join(par.text for par in doc.paragraphs)
    except PackageNotFoundError:
        # Nope, try text.
        with open(fn, "r") as f:
            text = f.read()

    return text


def _parse_testgen_mc(text):
    """Parse Pearson TestGen multiple choice questions.

    Parse text from Pearson TestGen for multiple choice questions,
    returning the questions and answers as a list of dicts.

    This code was developed specifically for test resources provided
    as Microsoft Word DOCX files with one textbook and may not be a
    portable grammar to parse all Pearson TestGen formats for multiple
    choice questions, but it should point in the correct direction.
    The output is also specific to the original materials and usage in
    the author's courses.  If format variations are found, file an
    issue at https://github.com/jeremyagray/vocutil/issues with sample
    unparseable questions and this grammar and its output can be
    generalized.

    Parameters
    ----------
    text : str
        The TestGen generated text to be parsed.

    Returns
    -------
    list[dict]
        The multiple choice questions.
    """
    # Pyparsing grammar.
    question = pp.Suppress(pp.Regex(r"\d+\)\s*")) + pp.rest_of_line().setResultsName(
        "question"
    )

    choice = (
        pp.Regex(r"[A-Z]").setResultsName("choices", listAllMatches=True)
        + pp.Suppress(pp.Regex(r"\)\s*"))
        + pp.rest_of_line().setResultsName("texts", listAllMatches=True)
    )

    answer = pp.Suppress(pp.Keyword("Answer:")) + pp.Regex(r"[A-Z]").setResultsName(
        "correct"
    )

    difficulty = pp.Suppress(
        pp.Keyword("Diff:") + pp.Regex(r"\d+").setResultsName("difficulty")
    )

    topic = (
        pp.Suppress(pp.Literal("Topic:"))
        + pp.Regex(r"\d+").setResultsName("chapter")
        + pp.Suppress(pp.Literal("."))
        + pp.Regex(r"\d+").setResultsName("section")
        + pp.Suppress(pp.rest_of_line())
    )

    blooms = pp.Suppress(pp.Keyword("Bloom's Taxonomy:") + pp.rest_of_line())

    exercise = (
        pp.Group(question + pp.OneOrMore(choice) + answer + difficulty + topic + blooms)
        .setResultsName("exercise", listAllMatches=True)
        .setDebug(flag=PYPARSING_DEBUG)
    )

    questions = []

    for tokens, start, end in exercise.scan_string(text):
        answers = []
        for c, t in zip(tokens[0].choices, tokens[0].texts):
            correct = True if c == tokens[0].correct else False
            answers.append(
                {
                    "answer": t,
                    "correct": correct,
                }
            )

        questions.append(
            {
                "question": tokens[0].question,
                "answers": answers,
                "chapter": tokens[0].chapter,
                "section": tokens[0].section,
            }
        )

    return questions


def load_testgen_mc(fn):
    """Load a Pearson TestGen multiple choice question bank.

    Load a Pearson TestGen multiple choice question bank from either a
    Microsoft Word DOCX or text file, returning the questions as a
    list of dicts, one per question and answer set.

    Each question is returned as a dict with the following format::

        {
            "question": "question text",
            "answers": [
                {
                    "answer": "answer text",
                    "correct": boolean,
                },
            ],
            "chapter": "chapter if available",
            "section": "section if available",
        }

    Parameters
    ----------
    fn : str
        The TestGen filename containing the text to be parsed.

    Returns
    -------
    list[dict]
        The multiple choice questions.

    Raises
    ------
    FileNotFoundError
        Raised on a non-existent file from underlying code.
    """
    return _parse_testgen_mc(_load_testgen_file(fn))
