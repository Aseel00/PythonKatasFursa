import unittest
from katas.word_count import count_words

class TestWordCount(unittest.TestCase):
    def test_empty_sen(self):
        self.assertEqual(count_words(""),0)
    def test_single_word(self):
        self.assertEqual(count_words("abvhfui"),1)
    def test_words(self):
        self.assertEqual(count_words("abc def ghi"),3)