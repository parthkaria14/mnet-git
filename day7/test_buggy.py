import unittest
from io import StringIO
from unittest.mock import patch

from buggy import divide, get_first, to_number


class TestDivide(unittest.TestCase):
    def test_normal_integer_division(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_normal_negative_division(self):
        self.assertEqual(divide(-10, 2), -5.0)

    def test_normal_float_result(self):
        self.assertEqual(divide(7, 2), 3.5)

    def test_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0.0)

    @patch("sys.stdout", new_callable=StringIO)
    def test_divide_by_zero_returns_none(self, _):
        self.assertIsNone(divide(10, 0))

    @patch("sys.stdout", new_callable=StringIO)
    def test_divide_by_zero_prints_error(self, mock_stdout):
        divide(10, 0)
        self.assertIn("Cannot divide by zero", mock_stdout.getvalue())


class TestGetFirst(unittest.TestCase):
    def test_normal_list(self):
        self.assertEqual(get_first([1, 2, 3]), 1)

    def test_single_element_list(self):
        self.assertEqual(get_first([42]), 42)

    def test_string_elements(self):
        self.assertEqual(get_first(["a", "b"]), "a")

    def test_none_as_first_element(self):
        self.assertIsNone(get_first([None, 2, 3]))

    @patch("sys.stdout", new_callable=StringIO)
    def test_empty_list_returns_none(self, _):
        self.assertIsNone(get_first([]))

    @patch("sys.stdout", new_callable=StringIO)
    def test_empty_list_prints_error(self, mock_stdout):
        get_first([])
        self.assertIn("List is empty", mock_stdout.getvalue())


class TestToNumber(unittest.TestCase):
    def test_normal_positive_integer(self):
        self.assertEqual(to_number("42"), 42)

    def test_zero_string(self):
        self.assertEqual(to_number("0"), 0)

    def test_negative_integer(self):
        self.assertEqual(to_number("-5"), -5)

    def test_whitespace_padded_integer(self):
        self.assertEqual(to_number("  10  "), 10)

    @patch("sys.stdout", new_callable=StringIO)
    def test_non_numeric_string_returns_none(self, _):
        self.assertIsNone(to_number("hello"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_empty_string_returns_none(self, _):
        self.assertIsNone(to_number(""))

    @patch("sys.stdout", new_callable=StringIO)
    def test_float_string_returns_none(self, _):
        self.assertIsNone(to_number("3.14"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_string_prints_error(self, mock_stdout):
        to_number("hello")
        self.assertIn("not a valid integer", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
