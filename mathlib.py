#!/usr/bin/env python3

"""
Math library for calculator.
"""

__author__ = "Mark Birger, Daniil Khudiakov, Martin Knotek"
__date__ = "26 Apr 2015"
__credits__ = ["Mark Birger", "Daniil Khudiakov", "Martin Knotek"]

__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "Mark Birger"
__status__ = "Development"

import math
import re

MATH_NAMESPACE = vars(math).copy()
MATH_NAMESPACE['__builtins__'] = None

DIGIT = r"([\-\+]?\d+(\.\d+)?)"
LEFT = r"[\(\~]"
RIGHT = r"[\)\!]"
OPERANDS = r"[\+\-\*\/\^\%]"

DIG = r"\d+(\.\d+)?"
VALUE = LEFT+r"*"+DIGIT+RIGHT+r"*"

# TODO: expression for substitution feature
# TAG = r"(\#[1-9][0-9]?)"
# DIG = r"\d+(\.\d+)?"
# VALUE = LEFT+r"*("+DIGIT+r"|"+TAG+r")"+RIGHT+r"*"

UNIT = r"("+VALUE+r"|("+OPERANDS+VALUE+r"))*"
REGEX_ALL = r"^"+VALUE+r"("+OPERANDS+VALUE+r")*$"
VALID_PATTERN = re.compile(REGEX_ALL)

def evaluate(expression, story):
    """
    Function evaluates literal. Full syntax description in user manual.
    @param expression string with an expression
    @param story array with another calculations (TODO)
    @result string with result or None if input is invalid
    """
    if expression is None:
        return None
    print("STORY:", story)
    expression = expression
    namespace = MATH_NAMESPACE
    namespace["evaluate"] = evaluate
    namespace["story"] = story
    try:
        if VALID_PATTERN.match(expression):
            expression = "("+expression+")"
            while True:
                expression = re.sub(
                    r'(\~('+DIGIT+'))', "("+r'\1'+")", expression)
                expression = re.sub(r'('+DIG+'!)', "("+r'\1'+")", expression)
                expression = re.sub(
                    r'('+DIG+r'\^('+DIGIT+'))', "("+r'\1'+")", expression)
                oldexpr = expression
                subexpr = re.sub(r'(.*)(\([^\(\)]+\))(.*)', r'\2', expression)
                subexpr = re.sub(r'\~('+DIGIT+')', "floor("+r'\1'+")", subexpr)
                subexpr = re.sub(
                    r'('+DIG+r')\^('+DIGIT+')',
                    "pow("+r'\1'+","+r'\3'+")", subexpr)
                subexpr = re.sub(r'('+DIG+')!', "factorial("+r'\1'+")", subexpr)

                # TODO: expression for substitution feature
                # substitution for story
                # if re.findall(r'\#[1-9][0-9]?', subexpr):
                    # namespace["story"] = [None] + \
                    # [float(i[1]) if i[1] is not None else i[1] for i in story]
                    # print(namespace["story"])
                    # print(namespace["story"][1])
                    # subexpr=re.sub(r'\#([1-9][0-9]?)',
                    # r'evaluate(story[\1], story)',subexpr)
                    # print("INPUT EVAL:", subexpr,end=" ")

                subresult = eval(subexpr, namespace)

                subresult = int(subresult) \
                    if int(subresult) == float(subresult) \
                    else round(float(subresult), 8)
                expression = re.sub(
                    r'(.*)(\([^\(\)]+\))(.*)',
                    r'\1'+"\""+str(subresult)+"\""+r'\3', expression)
                expression = re.sub(
                    "\""+str(subresult)+"\"",
                    str(subresult), expression)
                if oldexpr == expression:
                    break

            # TODO: expression for substitution feature
            # if re.findall(r'\#[1-9][0-9]?', expression):
                # print(namespace["story"])
                # namespace["story"] = [None] + [float(i[1]) \
                #   if i[1] is not None else i[1] for i in story]
                # print(namespace["story"])
                # expression=re.sub(r'\#([1-9][0-9]?)', \
                #   r'evaluate(story[\1])',expression)
            result = eval(expression, namespace)
            result = int(result) if int(result) == float(result)\
                else round(float(result), 8)
            print("RESULT:", result)
            return str(result)
        return None
    except Exception:
        return None
