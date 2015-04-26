#!/usr/bin/env python3

"""
Tests of calculation module.
"""

import unittest

from mathlib import evaluate

class BasicOperations(unittest.TestCase):
    def test_basic(self):
        story = []
        self.assertEqual(evaluate("4+5", story), "9")
        self.assertEqual(evaluate("5-4", story), "1")
        self.assertEqual(evaluate("-3-6", story), "-9")
        self.assertEqual(evaluate("+5+1", story), "6")
        self.assertEqual(evaluate("4*5", story), "20")
        self.assertEqual(evaluate("-4*5", story), "-20")
        self.assertEqual(evaluate("1/5", story), "0.2")
        self.assertEqual(evaluate("1/1", story), "1")

        self.assertEqual(evaluate("3+(5+5)", story), "13")
        self.assertEqual(evaluate("3*(5+5)", story), "30")
        self.assertEqual(evaluate("(5-5+2)", story), "2")
        self.assertEqual(evaluate("((6)-5)", story), "1")

        self.assertEqual(evaluate("0.2-0.55", story), "-0.35")

        self.assertEqual(evaluate("7!", story), "5040")
        self.assertEqual(evaluate("0!", story), "1")

        self.assertEqual(evaluate("4^4", story), "256")
        self.assertEqual(evaluate("4^4!", story), "281474976710656")
        self.assertEqual(evaluate("|+43|", story), "43")
        self.assertEqual(evaluate("|0.5-20|", story), "19.5")
        self.assertEqual(evaluate("||5+5||", story), "10")
        self.assertEqual(evaluate("|(33+52|)", story), "WTF")
        self.assertEqual(evaluate("|(32-52)|", story), "20")
        self.assertEqual(evaluate("4^(4)", story), "256")
        self.assertEqual(evaluate("(2^2)!", story), "24")
        self.assertEqual(evaluate("|4+4|!", story), "40320")
        

        self.assertEqual(evaluate("", story), None)
        self.assertEqual(evaluate("1/0", story), None)
        self.assertEqual(evaluate("65+", story), None)
        self.assertEqual(evaluate("(((23))", story), None)
        #|5454+54)

if __name__ == '__main__':
    unittest.main()