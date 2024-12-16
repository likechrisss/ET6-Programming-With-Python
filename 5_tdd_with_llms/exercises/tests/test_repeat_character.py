import unittest
from ..repeat_character import repeat_character

class TestRepeatCharacter(unittest.TestCase):
    def test_abcabc_a_3(self):
        # Expected: "abcabc" with 'a' repeated 3 times -> "aaabcaaabc"
        self.assertEqual(repeat_character("abcabc", "a", 3), "aaabcaaabc")
    def test_evan_n_2(self):
        self.assertEqual(repeat_character("evan", "n", 2), "evannn")

    def test_hello_x_4(self):
        # 'x' not in 'hello', should remain unchanged
        self.assertEqual(repeat_character("hello", "x", 4), "hello")

    def test_empty_string_a_5(self):
        # empty string remains empty
        self.assertEqual(repeat_character("", "a", 5), "")

    def test_zzz_z_1(self):
        # repeating 'z' once in 'zzz' should stay 'zzz'
        self.assertEqual(repeat_character("zzz", "z", 1), "zzz")
        
    def test_haiti_i_2_middle_only(self):
        # For "Haiti":
        # H (0) a(1) i(2) t(3) i(4)
        # Repeat only the middle i (index 2) twice, not the last i.
        # Expected result: "Haiiti"
        self.assertEqual(repeat_character("Haiti", "i", 2), "Haiiti")

if __name__ == "__main__":
    unittest.main()
