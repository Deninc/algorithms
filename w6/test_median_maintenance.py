import unittest
import median_maintenance as m

class Test(unittest.TestCase):

    def test_heap_min(self):
        data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
        n = len(data)
        heap_min = m.Heap()

        for x in data:
            heap_min.push(x)

        sort_min = [heap_min.pop() for _ in range(n)]
        self.assertEqual(sort_min, [0,1,2,3,4,5,6,7,8,9])

    def test_heap_max(self):
        data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
        n = len(data)
        heap_max = m.Heap(min_heap=False)

        for x in data:
            heap_max.push(x)

        sort_max = [heap_max.pop() for _ in range(n)]
        self.assertEqual(sort_max, [9,8,7,6,5,4,3,2,1,0])

    def test_medians(self):
        stream = [2,1,5,4,6,3]
        res = [2, 1, 2, 2, 4, 3]
        self.assertEqual(m.get_medians(stream), res)

if __name__ == "__main__":
    unittest.main()
