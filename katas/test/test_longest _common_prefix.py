import unittest
from katas.longest_common_prefix import longest_common_prefix

class TestLongestCommonPrefix(unittest.TestCase):
    def test_empty_set(self):
        self.assertEqual(longest_common_prefix([]),"")
    def test_empty_str(self):
        self.assertEqual(longest_common_prefix(["abc",""]),"")
    def test_single_str(self):
        self.assertEqual(longest_common_prefix(["abc"]),"abc")
    def test_one(self):
        self.assertEqual(longest_common_prefix(["abc","def"]),"")
    def test_two(self):
        self.assertEqual(longest_common_prefix(["abc","abcdef"]),"abc")
    def test_three(self):
        self.assertEqual(longest_common_prefix(["abcd","abef"]),"ab")

