import unittest

from ..mystery_2 import mystery_2

class TestMystery2(unittest.TestCase):
    """Test suite for the mystery_2 function."""

    def test_empty_list(self):
        """It should return None for an empty list."""
        self.assertEqual(mystery_2([]), None)

    def test_non_empty_list(self):
        """It should return the length of the list for non-empty input."""
        self.assertEqual(mystery_2([1, 2, 3]), 3)

    def test_invalid_string_input(self):
        """It should raise a TypeError for string input."""
        with self.assertRaises(TypeError):
            mystery_2('')

if __name__ == "__main__":
    unittest.main()
