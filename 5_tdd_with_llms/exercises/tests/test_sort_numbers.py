import unittest
from sort_numbers import sort_numbers  # We'll create sort_numbers.py next

class TestSortNumbers(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_numbers([]), [], "Sorting an empty list should return an empty list.")

    def test_single_element(self):
        self.assertEqual(sort_numbers([42]), [42], "Sorting a single-element list should return the same list.")

    def test_already_sorted(self):
        self.assertEqual(sort_numbers([1,2,3]), [1,2,3], "Already sorted list should remain unchanged.")

    def test_reverse_order(self):
        self.assertEqual(sort_numbers([3,2,1]), [1,2,3], "Should sort a reverse-ordered list.")

    def test_unsorted_list(self):
        self.assertEqual(sort_numbers([10, -2, 5, 0]), [-2, 0, 5, 10], "Should sort a mixed list.")

    def test_no_side_effects(self):
        original = [3, 1, 2]
        sorted_version = sort_numbers(original)
        self.assertEqual(sorted_version, [1,2,3], "Should return a sorted list.")
        self.assertEqual(original, [3,1,2], "Original list should remain unchanged.")

if __name__ == "__main__":
    unittest.main()
