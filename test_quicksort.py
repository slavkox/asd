import unittest
from quicksort import quicksort

class TestQuicksort(unittest.TestCase):
    def test_random(self):
        self.assertEqual(quicksort([3,6,8,10,1,2,1]), [1,1,2,3,6,8,10])

    def test_sorted(self):
        self.assertEqual(quicksort([1,2,3,4,5]), [1,2,3,4,5])

    def test_reverse_sorted(self):
        self.assertEqual(quicksort([5,4,3,2,1]), [1,2,3,4,5])

    def test_duplicates(self):
        self.assertEqual(quicksort([5,1,2,1,5,3]), [1,1,2,3,5,5])

    def test_empty(self):
        self.assertEqual(quicksort([]), [])

    def test_identical_elements(self):
        self.assertEqual(quicksort([4, 4, 4, 4]), [4, 4, 4, 4])
if __name__ == '__main__':
    unittest.main()
