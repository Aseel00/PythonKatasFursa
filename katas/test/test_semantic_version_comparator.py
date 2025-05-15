import unittest
from katas.semantic_version_comparator import compare_versions  # Replace 'your_module' with actual module name if needed

class TestCompareVersions(unittest.TestCase):

    def test_equal_versions(self):
        self.assertEqual(compare_versions("1.0.0", "1.0.0"), 0)
        self.assertEqual(compare_versions("2.3", "2.3.0"), 0)
        self.assertEqual(compare_versions("0.0.1", "0.0.1"), 0)

    def test_version1_greater(self):
        self.assertEqual(compare_versions("1.0.1", "1.0.0"), 1)
        self.assertEqual(compare_versions("2.0.0", "1.9.9"), 1)
        self.assertEqual(compare_versions("1.2.0", "1.1.9"), 1)
        self.assertEqual(compare_versions("1.0.10", "1.0.2"), 1)

    def test_version2_greater(self):
        self.assertEqual(compare_versions("1.0.0", "1.0.1"), -1)
        self.assertEqual(compare_versions("0.9.9", "1.0.0"), -1)
        self.assertEqual(compare_versions("1.2.0", "1.3.0"), -1)
        self.assertEqual(compare_versions("1.0.2", "1.0.10"), -1)

    def test_different_lengths(self):
        self.assertEqual(compare_versions("1.0", "1.0.0"), 0)
        self.assertEqual(compare_versions("1.0", "1.0.1"), -1)
        self.assertEqual(compare_versions("1.0.1", "1.0"), 1)
        self.assertEqual(compare_versions("1", "1.0.0"), 0)
        self.assertEqual(compare_versions("1.0.0.1", "1"), 1)


