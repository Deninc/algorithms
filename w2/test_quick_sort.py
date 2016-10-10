import unittest
from quick_sort import choose_pivot, partition, quick_sort

class TestQuickSort(unittest.TestCase):

    def test_partition(self):
        arr = [4,2,8,5,7,1]
        i = partition(arr, 0, 5)
        self.assertEqual(arr[i], 4)

    def test_quick_sort(self):
        arr = [8,2,4,5,7,1]
        quick_sort(arr)
        self.assertEqual(arr, [1,2,4,5,7,8])
        arr = [3,9,8,4,6,10,2,5,7,1]
        quick_sort(arr)
        self.assertEqual(arr, [1,2,3,4,5,6,7,8,9,10])

if __name__ == '__main__':
    unittest.main()
