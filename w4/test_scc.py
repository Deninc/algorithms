import unittest
import scc
from collections import defaultdict

test1 = """0 2
0 3
1 0
2 1
3 4"""

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

    def test_dfs_stack(self):
        g = scc.Graph(5)
        lines = test1.split("\n")
        for l in lines:
            arr = l.split()
            g.add_edge(int(arr[0]), int(arr[1]))
        self.assertEqual(g.dfs_stack(), [1,2,4,3,0])

    def test_reverse(self):
        d = defaultdict(list, {0: [2,3], 1: [0,], 2:[1,], 3:[4,]})
        g = scc.Graph(5, d)
        self.assertEqual(g.reverse(), {0: [1], 1: [2], 2: [0], 3: [0], 4: [3]})

    def test_scc(self):
        g = scc.Graph(10)
        lines = test2.split("\n")
        for l in lines:
            arr = l.split()
            g.add_edge(int(arr[0]), int(arr[1]))
        g.scc()

if __name__ == "__main__":
    unittest.main()
