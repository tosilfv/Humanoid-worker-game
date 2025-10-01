import unittest
from src.utils.constants import *

class TestConstants(unittest.TestCase):
    def test_screen_wid(self):
        self.assertEqual(SCREEN_WID, 800)

    def test_screen_hgt(self):
        self.assertEqual(SCREEN_HGT, 800)

    def test_screen_tra(self):
        self.assertEqual(SCREEN_TRA, 0)

    def test_const_x(self):
        self.assertEqual(CONST_X, "x")

    def test_const_y(self):
        self.assertEqual(CONST_Y, "y")

    def test_const_light(self):
        self.assertEqual(CONST_LIGHT, "light")

    def test_const_regular(self):
        self.assertEqual(CONST_REGULAR, "regular")

    def test_const_heavy(self):
        self.assertEqual(CONST_HEAVY, "heavy")
