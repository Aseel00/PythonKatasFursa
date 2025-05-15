import unittest
from katas.sliding_window_maximum import max_sliding_window  # Replace with actual module if needed

class TestMaxSlidingWindow(unittest.TestCase):

    def test_window_size_1(self):
        self.assertEqual(
            max_sliding_window([4, 2, 12, 3], 1),
            [4, 2, 12, 3]
        )

    def test_all_same_elements(self):
        self.assertEqual(
            max_sliding_window([5, 5, 5, 5, 5], 2),
            [5, 5, 5, 5]
        )

    def test_increasing_order(self):
        self.assertEqual(
            max_sliding_window([1, 2, 3, 4, 5], 3),
            [3, 4, 5]
        )

    def test_empty_input(self):
        self.assertEqual(
            max_sliding_window([], 3),
            []
        )

    def test_window_size_zero(self):
        self.assertEqual(
            max_sliding_window([1, 2, 3], 0),
            []
        )

    def test_window_size_equals_one_element(self):
        self.assertEqual(
            max_sliding_window([10], 1),
            [10]
        )


