import unittest

from buggy_fixed import avg, reverse_string


class TestAvg(unittest.TestCase):
    # --- normal cases ---

    def test_avg_integers(self):
        self.assertEqual(avg([10, 20, 30]), 20.0)

    def test_avg_floats(self):
        self.assertAlmostEqual(avg([1.5, 2.5, 3.0]), 2.3333333333333335)

    def test_avg_single_element(self):
        self.assertEqual(avg([42]), 42.0)

    def test_avg_negative_numbers(self):
        self.assertEqual(avg([-10, 10]), 0.0)

    def test_avg_mixed_positive_and_negative(self):
        self.assertEqual(avg([-5, 0, 5, 10]), 2.5)

    # --- edge cases ---

    def test_avg_two_elements(self):
        self.assertEqual(avg([1, 3]), 2.0)

    def test_avg_large_list(self):
        self.assertEqual(avg(list(range(1, 101))), 50.5)

    def test_avg_zeros(self):
        self.assertEqual(avg([0, 0, 0]), 0.0)

    # --- error cases ---

    def test_avg_empty_list_returns_error_message(self):
        self.assertEqual(avg([]), "Error: cannot average an empty list")


class TestReverseString(unittest.TestCase):
    # --- normal cases ---

    def test_reverse_regular_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_palindrome(self):
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_reverse_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_reverse_with_special_characters(self):
        self.assertEqual(reverse_string("a!b@c"), "c@b!a")

    def test_reverse_mixed_case(self):
        self.assertEqual(reverse_string("AbCd"), "dCbA")

    # --- edge cases ---

    def test_reverse_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverse_single_character(self):
        self.assertEqual(reverse_string("x"), "x")

    def test_reverse_numeric_string(self):
        self.assertEqual(reverse_string("12345"), "54321")

    def test_reverse_unicode(self):
        self.assertEqual(reverse_string("caf\u00e9"), "\u00e9fac")

    # --- error cases ---

    def test_reverse_none_raises_type_error(self):
        with self.assertRaises(TypeError):
            reverse_string(None)


if __name__ == "__main__":
    unittest.main()
