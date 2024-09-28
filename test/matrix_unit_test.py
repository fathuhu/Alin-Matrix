import unittest
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import row_echelon, solve_linear_system

class TestMatrixOperations(unittest.TestCase):

    def test_add_matrices(self):
        # Test addition of matrices using numpy
        mat1 = np.array([[1, 2], [3, 4]])
        mat2 = np.array([[5, 6], [7, 8]])
        result = np.add(mat1, mat2)
        expected = np.array([[6, 8], [10, 12]])
        np.testing.assert_array_equal(result, expected)

    def test_multiply_matrices(self):
        # Test multiplication of matrices using numpy
        mat1 = np.array([[1, 2], [3, 4]])
        mat2 = np.array([[5, 6], [7, 8]])
        result = np.dot(mat1, mat2)
        expected = np.array([[19, 22], [43, 50]])
        np.testing.assert_array_equal(result, expected)

    def test_transpose_matrix(self):
        # Test transpose of a matrix using numpy
        mat = np.array([[1, 2], [3, 4]])
        result = np.transpose(mat)
        expected = np.array([[1, 3], [2, 4]])
        np.testing.assert_array_equal(result, expected)

    def test_determinant_matrix(self):
        # Test determinant of a matrix using numpy
        mat = np.array([[1, 2], [3, 4]])
        result = np.linalg.det(mat)
        expected = -2
        self.assertAlmostEqual(result, expected)

    def test_inverse_matrix(self):
        # Test inverse of a matrix using numpy
        mat = np.array([[1, 2], [3, 4]])
        result = np.linalg.inv(mat)
        expected = np.array([[-2. ,  1. ],
                             [ 1.5, -0.5]])
        np.testing.assert_almost_equal(result, expected)

    def test_row_echelon(self):
        # Test row echelon form (assuming row_echelon is defined in app.py)
        mat = np.array([[1, 2, -1], [2, 3, 1], [-3, -1, 2]])
        result = row_echelon(mat)
        expected = np.array([[1, 2, -1], [0, -1, 3], [0, 0, 1]])  # Sesuaikan dengan hasil row echelon yang benar
        np.testing.assert_array_almost_equal(result, expected)

    def test_solve_linear_system(self):
        # Test solving linear systems (assuming solve_linear_system is defined in app.py)
        A = np.array([[2, -1], [1, 1]])
        b = np.array([0, 3])
        result = solve_linear_system(A, b)
        expected = np.array([1, 2])  # Sesuaikan dengan hasil solusi yang benar
        np.testing.assert_array_almost_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
