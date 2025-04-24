import unittest
from katas.true_counter import count_true_values

class TestTrueCounter(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count_true_values([]),0)
    def test_all_false(self):
        self.assertEqual(count_true_values([False,False]),0)
    def test_all_true(self):
        self.assertTrue(count_true_values([True,True]),2)
    def test_mixed(self):
        self.assertEqual(count_true_values([True,False,True,False]),2)
