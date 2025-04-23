import unittest
from katas.list_diff import find_difference

class TestListDiff(unittest.TestCase):
    def test_single_num(self):
        self.assertEqual(find_difference([5]),0)
    def test_empty_list(self):
        self.assertEqual(find_difference([]),0)
    def test_list(self):
        self.assertEqual(find_difference([1,3,800]),799)
    def test_negative_nums(self):
        self.assertEqual(find_difference([-8000,0,1]),8001)



