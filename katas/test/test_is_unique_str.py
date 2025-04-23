import unittest
from PythonKatasFursa.katas.is_unique_str import is_unique

class TestIsUnique(unittest.TestCase):
    def test_all_unique(self):
        self.assertTrue(is_unique("opal"))
    def test_empty_str(self):
        self.assertTrue(is_unique(""))
    def test_short_str(self):
        self.assertTrue(is_unique("a"))
    def test_not_unique(self):
        self.assertFalse(is_unique("hello"))



