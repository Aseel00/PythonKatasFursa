import unittest
from katas.reduce_list import reduce_array

class TestReduceList(unittest.TestCase):
    def test_empty(self):
        array=[]
        reduce_array(array)
        self.assertEqual(array,[])
    def test_1(self):
        array=[5,10]
        reduce_array(array)
        self.assertEqual(array,[5,5])
    def test_2(self):
        array=[3,-5,7]
        reduce_array(array)
        self.assertEqual(array,[3,-8,12])