#!/usr/bin/env python3

"""
Tests of calculation module.
"""

__author__ = "Mark Birger, Daniil Khudiakov, Martin Knotek"
__date__ = "26 Apr 2015"
__credits__ = ["Mark Birger", "Daniil Khudiakov", "Martin Knotek"]

__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "Mark Birger"
__status__ = "Production"

import unittest

from mathlib import evaluate

STORY = []

class Mathlibtests(unittest.TestCase):
    """
    Class implements different tests of the math library.
    """
    def test_basic(self):
        """
        Basic operations tests.
        """
        self.assertEqual(evaluate("4+5", STORY), "9")
        self.assertEqual(evaluate("5-4", STORY), "1")
        self.assertEqual(evaluate("-3-6", STORY), "-9")
        self.assertEqual(evaluate("+5+1", STORY), "6")
        self.assertEqual(evaluate("4*5", STORY), "20")
        self.assertEqual(evaluate("-4*5", STORY), "-20")
        self.assertEqual(evaluate("1/5", STORY), "0.2")
        self.assertEqual(evaluate("1/1", STORY), "1")

    def test_brackets(self):
        """
        Brackets tests.
        """
        self.assertEqual(evaluate("3+(5+5)", STORY), "13")
        self.assertEqual(evaluate("3*(5+5)", STORY), "30")
        self.assertEqual(evaluate("(5-5+2)", STORY), "2")
        self.assertEqual(evaluate("((6)-5)", STORY), "1")
        self.assertEqual(evaluate("(12*(6-3)/6)", STORY), "6")

    def test_float(self):
        """
        Tests with float numbers.
        """
        self.assertEqual(evaluate("0.2+0.55", STORY), "0.75")
        self.assertEqual(evaluate("0.2-0.55", STORY), "-0.35")
        self.assertEqual(evaluate("0.2*0.55", STORY), "0.11")
        self.assertEqual(evaluate("0.2/0.5", STORY), "0.4")

    def test_factorial(self):
        """
        Tests for factorial function.
        """
        self.assertEqual(evaluate("7!", STORY), "5040")
        self.assertEqual(evaluate("0!", STORY), "1")
        # self.assertEqual(evaluate("3.3!", STORY), "362880")
        self.assertEqual(evaluate("3!!", STORY), "720")
        self.assertEqual(evaluate("3!!+3!", STORY), "726")
        self.assertEqual(evaluate("(3!+3)!", STORY), "362880")
        self.assertEqual(evaluate("((4-4)+(4-2)*2)!", STORY), "24")

    def test_pow(self):
        """
        Tests for power function.
        """
        self.assertEqual(evaluate("0^0", STORY), "1")
        self.assertEqual(evaluate("4^4", STORY), "256")
        self.assertEqual(evaluate("4^-4", STORY), "0.00390625")
        self.assertEqual(evaluate("4^0.4", STORY), "0.00390625")
        self.assertEqual(evaluate("4^-0.4", STORY), "256")
        self.assertEqual(evaluate("4^(4-2)", STORY), "16")
        self.assertEqual(evaluate("((4-4)+4)^((4-4)+4)", STORY), "256")

    def test_abs(self):
        """
        Tests for absolute function.
        """
        self.assertEqual(evaluate("|+43|", STORY), "43")
        self.assertEqual(evaluate("|0.5-20|", STORY), "19.5")
        self.assertEqual(evaluate("||5+5||", STORY), "10")
        self.assertEqual(evaluate("|(32-52)|", STORY), "20")

    def test_hard(self):
        """
        Hard test cases.
        """
        self.assertEqual(evaluate("(2^2)!", STORY), "24")
        self.assertEqual(evaluate("|4+4|!", STORY), "40320")
        self.assertEqual(evaluate("4^4!", STORY), "281474976710656")
        self.assertEqual(evaluate("||3!-4^4|*-12|/6", STORY), "500")
            
    def test_invalid(self):
        """
        Test cases, where evaluation is impossible.
        """
        self.assertEqual(evaluate("", STORY), None)
        self.assertEqual(evaluate("1/0", STORY), None)
        self.assertEqual(evaluate("65+", STORY), None)
        self.assertEqual(evaluate("*65", STORY), None)
        self.assertEqual(evaluate("(((23))", STORY), None)
        self.assertEqual(evaluate("|23)", STORY), None)
        self.assertEqual(evaluate("|(33+52|)", STORY), None)
        self.assertEqual(evaluate("|5454+54)", STORY), None)

if __name__ == '__main__':
    unittest.main()
