import unittest
from katas.max_storage_capacity import max_storage_area  # Adjust this path based on your project structure

class TestMaxStorageArea(unittest.TestCase):

    def test_single_container(self):
        self.assertEqual(max_storage_area([4]), 4)

    def test_uniform_height(self):
        self.assertEqual(max_storage_area([2, 2, 2, 2]), 8)

    def test_strictly_increasing(self):
        self.assertEqual(max_storage_area([1, 2, 3, 4, 5]), 9)

    def test_mixed_heights(self):
        self.assertEqual(max_storage_area([6, 2, 5, 4, 5, 1, 6]), 12)

    def test_all_zeros(self):
        self.assertEqual(max_storage_area([0, 0, 0]), 0)

    def test_empty_input(self):
        self.assertEqual(max_storage_area([]), 0)

