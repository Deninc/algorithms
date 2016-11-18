import unittest
import shortest_path as sp

t1 = """1	2,1	8,2

2	1,1	3,1

3	2,1	4,1

4	3,1	5,1

5	4,1	6,1

6	5,1	7,1

7	6,1	8,1

8	7,1	1,2"""

r1 = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 4, 7: 3, 8: 2}

t2 = """1	2,4	3,2
2	1,4	3,1	4,7	6,1	7,1	10,1
3	1,2	2,1	4,5	9,6	10,2
4	2,7	3,5	5,3	6,2
5	4,3	6,5	8,4	9,5
6	2,1	4,2	5,5	8,3
7	2,1	8,2
8	5,4	6,3	7,2	10,2
9	3,6	5,5
10	2,1	3,2	8,2"""

r2 = {1: 0, 3: 2, 2: 3, 6: 4, 7: 4, 10: 4, 4: 6, 8: 6, 9: 8, 5: 9}

class TestShortestPath(unittest.TestCase):

    def test_heap(self):
        h = sp.Heap()
        h.add_vertex(2, 1)
        h.add_vertex(3, 4)
        v = h.pop_vertex()
        self.assertEqual(v, (2, 1))
        h.add_vertex(5, 0)
        h.remove_vertex(5)
        v = h.pop_vertex()
        self.assertEqual(v, (3, 4))

    def __read_test(self, graph, test):
        lines = test.split("\n")
        for l in lines:
            arr = l.split("\t")
            for adj in arr[1:]:
                v, w = adj.split(",")
                graph.add_edge(int(arr[0]), int(v), int(w))

    def test_shortest_path(self):
        g1 = sp.Graph(8)
        self.__read_test(g1, t1)
        self.assertEqual(g1.shortest_path(1), r1)

        g2 = sp.Graph(10)
        self.__read_test(g2, t2)
        self.assertEqual(g2.shortest_path(1), r2)

if __name__ == "__main__":
    unittest.main()
