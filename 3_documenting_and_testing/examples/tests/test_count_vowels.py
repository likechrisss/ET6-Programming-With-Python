import unittest
from count_vowels import count_vowels


#Added more comprehensive cases
class TestCountVowels(unittest.TestCase):
    """Test suite for the count_vowels function."""

    # Standard cases
    def test_empty_string(self):
        """It should return 0 for an empty string."""
        self.assertEqual(count_vowels(""), 0)
        
    def test_no_vowels(self):
        """It should return 0 for strings without vowels."""
        self.assertEqual(count_vowels("cry"), 0)
        self.assertEqual(count_vowels("12345"), 0)
        self.assertEqual(count_vowels("!@#$%^&*()"), 0)
        
    def test_all_vowels(self):
        """It should count all vowels in a string."""
        self.assertEqual(count_vowels("AUIO"), 4)
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)
        
    def test_mixed_case(self):
        """It should handle mixed case strings."""
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels("HELLO world"), 3)

    def test_special_characters(self):
        """It should ignore special characters and count only vowels."""
        self.assertEqual(count_vowels("h@e#l$l%o^"), 2)

    # Edge cases
    def test_single_vowel(self):
        """It should return 1 for a single vowel."""
        self.assertEqual(count_vowels("A"), 1)
        self.assertEqual(count_vowels("e"), 1)

    def test_single_consonant(self):
        """It should return 0 for a single consonant."""
        self.assertEqual(count_vowels("b"), 0)
        
    def test_whitespace(self):
        """It should count vowels correctly with whitespace."""
        self.assertEqual(count_vowels(" a e i o u "), 5)
        self.assertEqual(count_vowels(" h e l l o "), 2)

    # Defensive cases
    def test_not_string(self):
        """It should raise a TypeError for non-string input."""
        with self.assertRaises(TypeError):
            count_vowels(123)
        with self.assertRaises(TypeError):
            count_vowels(["a", "e", "i"])
        with self.assertRaises(TypeError):
            count_vowels(None)

if __name__ == '__main__':
    unittest.main()
