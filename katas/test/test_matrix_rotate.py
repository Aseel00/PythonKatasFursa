import unittest
from katas.matrix_rotate import rotate_matrix

class TestRotateMatrix(unittest.TestCase):
    def test_zeros(self):
        matrix=[[0,0,0],[0,0,0],[0,0,0]]
        rotate_matrix(matrix)
        self.assertEqual(matrix,[[0,0,0,],[0,0,0],[0,0,0]])
    def test_1(self):
        matrix2=[[1,2,3],[7,5,3],[9,5,1]]
        rotate_matrix(matrix2)
        self.assertEqual(matrix2,[[9,7,1],[5,5,2],[1,3,3]])
        print(matrix2)
    def test_2(self):
        matrix3=  [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
        rotate_matrix(matrix3)
        self.assertEqual(matrix3,[[7,4,1],[8,5,2],[9,6,3]])
