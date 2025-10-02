import unittest
from components import Info
from utils.constants import INFO_POS_X, INFO_POS_Y, BLACK


class TestInfo(unittest.TestCase):
    """Tests for Info class from components/Info."""

    def setUp(self):
        self.info = Info()

    def test_instance_of_info(self):
        self.assertIsInstance(self.info, Info)

    def test_create_info_text_xcor(self):
        loc_x = self.info.create_info_text.xcor()
        self.assertEqual(loc_x, INFO_POS_X)

    def test_create_info_text_ycor(self):
        loc_y = self.info.create_info_text.ycor()
        self.assertEqual(loc_y, INFO_POS_Y)

    def test_create_info_text_color(self):
        color = self.info.create_info_text.pencolor()
        self.assertEqual(color, BLACK)
