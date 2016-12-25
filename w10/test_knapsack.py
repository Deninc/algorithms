import unittest
from knapsack import knapsack

class TestKnapsack(unittest.TestCase):

    def test_small_knapsack(self):
        v = [3, 2, 4, 4]
        w = [4, 3, 2, 3]
        self.assertEqual(knapsack(v, w, 6), 8)

if __name__ == "__main__":
    unittest.main()
