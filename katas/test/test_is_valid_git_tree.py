import unittest
from katas.is_valid_git_tree import is_valid_git_tree

class TestIsValidGitTree(unittest.TestCase):

    def test_empty(self):
        self.assertFalse(is_valid_git_tree({}))
    def test_not_have_root(self):
        false_tree = {"A": ["B"], "C": ["D"], "B": [], "D": []}
        self.assertFalse(is_valid_git_tree(false_tree))
