import unittest
import scc
from collections import defaultdict

test2 = """1 4
2 8
3 6
4 7
5 2
6 9
7 1
8 6
8 5
9 7
9 3"""

class TestSCC(unittest.TestCase):

    def test_scc(self):
        d = defaultdict(list, {0: [2,3], 1: [0,], 2:[1,], 3:[4,]})
        g1 = scc.Graph(5, d)
        self.assertEqual(g1.scc(), [3,1,1])

        g2 = scc.Graph(10)
        lines = test2.split("\n")
        for l in lines:
            arr = l.split()
            g2.add_edge(int(arr[0]), int(arr[1]))
        self.assertEqual(g2.scc(), [3,3,3,1])

if __name__ == "__main__":
    unittest.main()
