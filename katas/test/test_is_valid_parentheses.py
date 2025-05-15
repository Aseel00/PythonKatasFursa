import unittest
from katas.is_valid_parentheses import is_valid_parentheses

class TestValidParentheses(unittest.TestCase):
    def test_valid_simple(self):
        self.assertTrue(is_valid_parentheses("()"))

    def test_valid_mixed(self):
        self.assertTrue(is_valid_parentheses("()[]{}"))

    def test_valid_nested(self):
        self.assertTrue(is_valid_parentheses("([{}])"))

    def test_invalid_wrong_order(self):
        self.assertFalse(is_valid_parentheses("(]"))

    def test_invalid_wrong_nesting(self):
        self.assertFalse(is_valid_parentheses("([)]"))

    def test_empty_string(self):
        self.assertTrue(is_valid_parentheses(""))

    def test_long_valid(self):
        self.assertTrue(is_valid_parentheses("(({}[()]))"))
