import unittest
from katas.requirements_coverage import select_minimal_test_cases

class TestSelectMinimalTestCases(unittest.TestCase):

    def test_example_case(self):
        test_cases = [
            [1, 2, 3],
            [1, 4],
            [2, 3, 4],
            [1, 5],
            [3, 5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertIn(result, [[2, 3], [3, 2]])

    def test_single_case_covers_all(self):
        test_cases = [
            [1, 2, 3]
        ]
        self.assertEqual(select_minimal_test_cases(test_cases), [0])

    def test_each_requirement_needs_separate_case(self):
        test_cases = [
            [1],
            [2],
            [3]
        ]
        self.assertEqual(select_minimal_test_cases(test_cases), [0, 1, 2])

    def test_multiple_minimal_solutions(self):
        test_cases = [
            [1, 2],
            [2, 3],
            [1, 3]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertIn(result, [[0, 1], [0, 2], [1, 2]])

    def test_duplicate_test_cases(self):
        test_cases = [
            [1, 2],
            [1, 2],
            [2, 3],
            [3]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertIn(result, [[0, 2], [1, 2]])

