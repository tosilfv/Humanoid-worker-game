import unittest
from unittest.mock import patch
from utils.helpers import direction_term, print_message


class TestDirectionTerm(unittest.TestCase):
    """Tests for direction_term from utils/helpers."""

    def test_get_one(self):
        self.assertEqual(direction_term(0, 1), 1)

    def test_get_minus_one(self):
        self.assertEqual(direction_term(1, 0), -1)


class TestPrintMessage(unittest.TestCase):
    """Tests for print_message from utils/helpers."""

    @patch('builtins.print')
    def test_print_hello_world(self, mock_print):
        print_message('Hello, World!')
        mock_print.assert_called_with('Hello, World!')
