import unittest
from katas.matrix_rotate import rotate_matrix

class TestRotateMatrix(unittest.TestCase):
    def test_zeros(self):
        matrix=[[0,0,0],[0,0,0],[0,0,0]]
        rotate_matrix(matrix)
        self.assertEqual(matrix,[[0,0,0,],[0,0,0],[0,0,0]])
    def test_1(self):
        matrix=[[1,2,3],[7,5,3],[9,5,1]]
        rotate_matrix(matrix)
        self.assertEqual(matrix,[[9,7,1],[5,5,2],[1,3,3]])
