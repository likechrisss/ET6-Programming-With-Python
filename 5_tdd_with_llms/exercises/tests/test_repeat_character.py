import unittest
from repeat_character import repeat_character

class TestRepeatCharacter(unittest.TestCase):
    def test_abcabc_a_3(self):
        # Expected: "abcabc" with 'a' repeated 3 times -> "aaabcaaabc"
        self.assertEqual(repeat_character("abcabc", "a", 3), "aaabcaaabc")

if __name__ == "__main__":
    unittest.main()
