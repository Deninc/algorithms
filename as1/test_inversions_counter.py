import unittest
from inversions_counter import count

class TestInversionsCounter(unittest.TestCase):

    def test_counter(self):
        arr = [1,3,5,2,4,6]
        self.assertEqual(count(arr), 5)


if __name__ == '__main__':
    unittest.main()
