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

"""Common Cartridge multiple response item."""

import json
from xml.etree.ElementTree import Element as ETElement  # nosec B405
from xml.etree.ElementTree import SubElement as ETSubElement  # nosec B405

import defusedxml.ElementTree as ET

from .item import Item


def _get_answer_states(conditionvar):
    """Get answer states from XML."""
    # QTI 1.2 ``or`` container.
    holder = conditionvar.find("or")
    if holder is not None:
        return {ele.text: True for ele in holder.findall("varequal")}

    # QTI 1.3 explicit ``and`` container.
    holder = conditionvar.find("and")
    if holder is not None:
        return {
            **{ele.text: True for ele in holder.findall("varequal")},
            **{ele.find("varequal").text: False for ele in holder.findall("not")},
        }

    # QTI 1.2 implicit ``and`` container.
    return {
        **{ele.text: True for ele in conditionvar.findall("varequal")},
        **{ele.find("varequal").text: False for ele in conditionvar.findall("not")},
    }


def _parse_answers(tree):
    """Parse the answers and their correctness from XML.

    Parameters
    ----------
    item : str
        IMSCC multiple response format XML.

    Returns
    -------
    dict
        Question and answer data.

    Answer choices are stored in the
    item->presentation->response_lid->render_choice element with the
    answer text stored in the text node of
    response_label->material->mattext subelement and the id in the
    ``ident`` attribute of the ``response_label`` element.

    The answer correctness data is stored in the
    item->resprocessing->respcondition->conditionvar in one of three
    ways:

    1. The ids of correct answers only in the text nodes of
    ``varequal`` subelements of an ``or`` element, per the QTI 1.2
    specification.
    2. The ids of correct answers in the text nodes of ``varequal``
    subelements and the ids of incorrect answers in the text nodes of
    ``varequal`` subelements within individual ``not`` subelements.
    This is the implicit ``and`` of the QTI 1.2 specification.
    3. The ids of correct answers in the text nodes of ``varequal``
    subelements and the ids of incorrect answers in the text nodes of
    ``varequal`` subelements within individual ``not`` subelements all
    within an explicit ``and`` subelement, per the current QTI 1.3
    specification.

    All three ways should be supported.
    """
    # Parse answers and ids.
    answers = {
        ele.get("ident"): {
            "answer": ele.find("material").find("mattext").text,
            "correct": False,
        }
        for ele in tree.find("presentation")
        .find("response_lid")
        .find("render_choice")
        .findall("response_label")
    }

    for k, v in _get_answer_states(
        tree.find("resprocessing").find("respcondition").find("conditionvar")
    ).items():
        answers[k]["correct"] = v

    return answers


class MultipleResponse(Item):
    """A Common Cartridge multiple response item."""

    def __init__(self, question, answers, **kwargs):
        """Initialize a ``MultipleResponse`` item.

        Initialize a ``MultipleResponse`` item.

        Parameters
        ----------
        question : str
            The HTML formatted question text.
        answers : [obj]
            The possible answers.
        """
        # Call the super.
        super().__init__(**kwargs)

        self.question = question
        self.answers = answers

        self.item = ETElement("item", ident=str(self.uuid))
        self.itemmetadata = ETSubElement(self.item, "itemmetadata")
        self.qtimetadata = ETSubElement(self.itemmetadata, "qtimetadata")
        self.qtimetadatafield = ETSubElement(self.qtimetadata, "qtimetadatafield")
        self.fieldlabel = ETSubElement(self.qtimetadatafield, "fieldlabel")
        self.fieldlabel.text = "cc_profile"
        self.fieldentry = ETSubElement(self.qtimetadatafield, "fieldentry")
        self.fieldentry.text = "cc.multiple_response.v0p1"
        self.presentation = ETSubElement(self.item, "presentation")
        self.material = ETSubElement(self.presentation, "material")
        self.mattext = ETSubElement(self.material, "mattext", texttype="text/html")
        self.mattext.text = question

        self.response = ETSubElement(
            self.presentation,
            "response_lid",
            ident=str(self.uuid),
            rcardinality="Multiple",
        )
        self.choices = ETSubElement(self.response, "render_choice")

        ans_states = {}
        for i, ans in enumerate(answers):
            ident = f"{self.uuid}-{i}"
            choice = ETSubElement(self.choices, "response_label", ident=ident)
            material = ETSubElement(choice, "material")
            mattext = ETSubElement(material, "mattext", texttype="text/html")
            mattext.text = ans["answer"]
            ans_states[ident] = ans["correct"]

        grade = ETSubElement(self.item, "resprocessing")
        outcomes = ETSubElement(grade, "outcomes")
        ETSubElement(
            outcomes,
            "decvar",
            maxvalue="100",
            minvalue="0",
            varname="SCORE",
            vartype="Decimal",
        )
        cond = ETSubElement(
            grade,
            "respcondition",
            attrib={
                "continue": "No",
            },
        )
        condvar = ETSubElement(cond, "conditionvar")
        combiner = ETSubElement(condvar, "and")

        for k, v in ans_states.items():
            if v:
                varequal = ETSubElement(combiner, "varequal", respident=str(self.uuid))
                varequal.text = k
            else:
                wrong = ETSubElement(combiner, "not")
                varequal = ETSubElement(wrong, "varequal", respident=str(self.uuid))
                varequal.text = k

        setvar = ETSubElement(cond, "setvar", action="Set", varname="SCORE")
        setvar.text = "100"

        return

    @classmethod
    def from_json(cls, item, **kwargs):
        """Create a ``MultipleResponse`` item from JSON data.

        Create a ``MultipleResponse`` item from JSON data.

        Parameters
        ----------
        cls
            The ``MultipleResponse`` class.
        item : str
            A string containing JSON multiple response data.
        """
        data = json.loads(item)

        return cls(data["question"], data["answers"], **kwargs)

    @classmethod
    def from_xml(cls, item, **kwargs):
        """Create a ``MultipleResponse`` item from XML data.

        Create a ``MultipleResponse`` item from XML data.

        Parameters
        ----------
        cls
            The ``MultipleResponse`` class.
        item : str
            A string containing IMSCC multiple response XML data.
        """
        tree = ET.fromstring(item)

        return cls(
            tree.find("presentation").find("material").find("mattext").text,
            _parse_answers(tree),
            **kwargs,
        )

    def to_json(self):
        """Create a multiple response JSON string from item data."""
        return json.dumps(
            {
                "type": "multiple response",
                "question": self.mattext.text,
                "answers": [
                    {
                        "answer": ans["answer"],
                        "correct": ans["correct"],
                    }
                    for ans in _parse_answers(self.item).values()
                ],
            }
        )

    def to_xml(self):
        """Create a multiple response XML string from item data."""
        return ET.tostring(self.item, encoding="unicode")
