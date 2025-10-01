import unittest
from unittest.mock import patch
from src.utils.helpers import direction_term, print_message

class TestDirectionTerm(unittest.TestCase):
    def test_get_one(self):
        self.assertEqual(direction_term(0, 1), 1)

    def test_get_minus_one(self):
        self.assertEqual(direction_term(1, 0), -1)

class TestPrintMessage(unittest.TestCase):
    @patch('builtins.print')
    def test_print_hello_world(self, mock_print):
        print_message('Hello, World!')
        mock_print.assert_called_with('Hello, World!')
