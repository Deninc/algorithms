import unittest
from knapsack import knapsack, knapsack_re

class TestKnapsack(unittest.TestCase):

    def test_small_knapsack(self):
        v = [3, 2, 4, 4]
        w = [4, 3, 2, 3]
        self.assertEqual(knapsack(v, w, 6), 8)

        v = [4, 2, 6, 1, 2]
        w = [12, 1, 4, 1, 2]
        self.assertEqual(knapsack_re(v, w, 15), 11)

if __name__ == "__main__":
    unittest.main()
