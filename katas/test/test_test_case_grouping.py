import unittest
from katas.test_case_grouping import group_test_cases  # replace with actual module name


class TestGroupTestCases(unittest.TestCase):

    def test_all_single(self):
        self.assertCountEqual(
            group_test_cases([1, 1, 1]),
            [[0], [1], [2]]
        )

    def test_all_same_size(self):
        self.assertCountEqual(
            group_test_cases([2, 2, 2, 2]),
            [[0, 1], [2, 3]]
        )

    def test_mixed_sizes(self):
        result = group_test_cases([2, 1, 2, 1])
        expected = [[0, 2], [1], [3]]
        self.assertCountEqual(result, expected)

    def test_empty(self):
        self.assertEqual(group_test_cases([]), [])



