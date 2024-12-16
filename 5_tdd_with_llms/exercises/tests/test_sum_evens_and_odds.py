import unittest
from sum_evens_and_odds import sum_evens_and_odds

class TestSumEvensAndOdds(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_evens_and_odds([]), {"even": 0, "odd": 0})

    def test_all_even(self):
        self.assertEqual(sum_evens_and_odds([2, 4, 6]), {"even": 12, "odd": 0})

    def test_all_odd(self):
        self.assertEqual(sum_evens_and_odds([1, 3, 5]), {"even": 0, "odd": 9})

    def test_mixed_numbers(self):
        # even: 2, 4 = 6
        # odd: 1, 3 = 4
        self.assertEqual(sum_evens_and_odds([1, 2, 3, 4]), {"even": 6, "odd": 4})

    def test_including_negatives(self):
        # evens: 2, -4 = -2
        # odds: -1, 3 = 2
        self.assertEqual(sum_evens_and_odds([-1, 2, -4, 3]), {"even": -2, "odd": 2})

if __name__ == "__main__":
    unittest.main()
