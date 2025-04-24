import unittest
from katas.sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(sum_of_digits("abc"),0)
    def test_single(self):
        self.assertEqual(sum_of_digits("1"),1)
    def test_mix(self):
        self.assertEqual(sum_of_digits("ab5c6"),11)