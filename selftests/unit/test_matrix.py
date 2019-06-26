from unittest import TestCase

from wordhunter.core.matrix import generate


class TestMatrix(TestCase):
    def test_matrix_size(self):
        matrix = generate(dimension=5)
        self.assertEquals(len(matrix), 5)
        for row in matrix:
            self.assertEquals(len(row), 5)

    def test_matrix_items(self):
        matrix = generate(dimension=10)
        for row in matrix:
            for item in row:
                self.assertIn(item, 'abcdefghijklmnopqrstuvwxyz')
