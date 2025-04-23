import unittest
from katas.list_flatten import flatten_list

class TestListFlat(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(len(flatten_list([])),0)
    def test_comp(self):
        self.assertEqual(flatten_list([[3],5,[[[8],[7]],4],[[2]],[]]),[3,5,8,7,4,2])

