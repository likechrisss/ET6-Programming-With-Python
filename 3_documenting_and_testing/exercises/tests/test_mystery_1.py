import unittest
from exercises.mystery_1 import mystery_1  # Adjust the import path as needed


class TestMystery1(unittest.TestCase):
<<<<<<< HEAD

    """Unit tests for the mystery_1 function."""

    def test_add_integers(self):
        self.assertEqual(mystery_1(2, 3), 5)

    def test_add_floats(self):
        self.assertEqual(mystery_1(1.5, 2.5), 4.0)

    def test_add_integer_and_float(self):
        self.assertEqual(mystery_1(2, 2.5), 4.5)

    def test_concatenate_strings(self):
        self.assertEqual(mystery_1("hello", " world"), "hello world")

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            mystery_1(2, "hello")
        with self.assertRaises(TypeError):
            mystery_1(1.5, "world")


if __name__ == "__main__":
    unittest.main()
=======
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_1(0, 0), 0)
>>>>>>> b2060ebfbf4cba94199c62e2f44ebf18a390d55e
