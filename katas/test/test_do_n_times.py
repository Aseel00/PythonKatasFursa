import unittest
import random
from katas from do_n_times


class TestDoNTimes(unittest.TestCase):
    def setUp(self):
        self.count=0
    def counter(self):
        self.count+=1
    def test_n_times(self):
        ran_num=random.randint(0,100)
        do_n_times(self.counter,ran_num)
        self.assertEqual(self.count,ran_num)
