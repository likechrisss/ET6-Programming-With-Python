import unittest
from mystery_3 import mystery_3

class TestMystery3(unittest.TestCase):
    """Test suite for the mystery_3 function."""

    def test_minimal_input(self):
        """It should handle the case where both inputs are zero."""
        self.assertEqual(mystery_3(0, 0), 0)

    def test_a_less_than_b(self):
        """It should return a when a < b."""
        self.assertEqual(mystery_3(2, 5), 2)

    def test_a_greater_than_b(self):
        """It should return b when a > b."""
        self.assertEqual(mystery_3(7, 3), 3)

    def test_a_equal_to_b(self):
        """It should return the sum of a and b when a == b."""
        self.assertEqual(mystery_3(4, 4), 8)

if __name__ == "__main__":
    unittest.main()
