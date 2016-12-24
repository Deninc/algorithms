import unittest
from mwis import mwis

class TestMWIS(unittest.TestCase):

    def test_1_vertex(self):
        self.assertEqual(mwis([1]), 1)

    def test_2_vertices(self):
        self.assertEqual(mwis([4, 2]), 4)

    def test_3_vertices(self):
        self.assertEqual(mwis([4, 5, 3]), 7)
        self.assertEqual(mwis([4, 8, 3]), 8)

    def test_n_vertices(self):
        self.assertEqual(mwis([6, 5, 3, 7]), 13)
        self.assertEqual(mwis([4, 5, 3, 6, 7]), 14)

if __name__ == "__main__":
    unittest.main()
