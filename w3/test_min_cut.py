import unittest
import min_cut

test1 = """1 4 2 7 3
2 4 1 3
3 1 2 4
4 5 1 2 3
5 8 7 6 4
6 8 5 7
7 6 8 5 1
8 7 6 5"""

test2 = """1 19 15 36 23 18 39
2 36 23 4 18 26 9
3 35 6 16 11
4 23 2 18 24
5 14 8 29 21
6 34 35 3 16
7 30 33 38 28
8 12 14 5 29 31
9 39 13 20 10 17 2
10 9 20 12 14 29
11 3 16 30 33 26
12 20 10 14 8
13 24 39 9 20
14 10 12 8 5
15 26 19 1 36
16 6 3 11 30 17 35 32
17 38 28 32 40 9 16
18 2 4 24 39 1
19 27 26 15 1
20 13 9 10 12
21 5 29 25 37
22 32 40 34 35
23 1 36 2 4
24 4 18 39 13
25 29 21 37 31
26 31 27 19 15 11 2
27 37 31 26 19 29
28 7 38 17 32
29 8 5 21 25 10 27
30 16 11 33 7 37
31 25 37 27 26 8
32 28 17 40 22 16
33 11 30 7 38
34 40 22 35 6
35 22 34 6 3 16
36 15 1 23 2
37 21 25 31 27 30
38 33 7 28 17 40
39 18 24 13 9 1
40 17 32 22 34 38"""

def read_test(test):
    res = {}
    lines = test.split("\n")
    for l in lines:
        arr = l.split()
        arr = map(int, arr)
        res[arr[0]] = arr[1:]
    return res

class TestMinCut(unittest.TestCase):

    def test_union_find(self):
        pass

    def test_min_cut(self):
        g = min_cut.Graph(read_test(test1))
        self.assertTrue(g.min_cut() == 2)

        g = min_cut.Graph(read_test(test2))
        self.assertTrue(g.min_cut() == 3)

if __name__ == "__main__":
    unittest.main()
