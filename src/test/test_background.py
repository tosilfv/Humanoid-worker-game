import unittest
from components import Background


class TestBackground(unittest.TestCase):
    """Tests for Background class from components/Background."""

    def setUp(self):
        self.background = Background()

    def test_background_part(self):
        self.assertEqual(len(self.background.background_part), 14)

    def test_left(self):
        self.assertEqual(self.background.left, True)

    def test_right(self):
        self.assertEqual(self.background.right, False)

    def test_is_light_lift_up(self):
        self.assertEqual(self.background.is_light_lift_up, False)

    def test_is_light_lift_down(self):
        self.assertEqual(self.background.is_light_lift_down, False)

    def test_is_regular_lift_up(self):
        self.assertEqual(self.background.is_regular_lift_up, False)

    def test_is_regular_lift_down(self):
        self.assertEqual(self.background.is_regular_lift_down, False)

    def test_is_heavy_lift_up(self):
        self.assertEqual(self.background.is_heavy_lift_up, False)

    def test_is_heavy_lift_down(self):
        self.assertEqual(self.background.is_heavy_lift_down, False)

    def test_is_conveyor_lift_up(self):
        self.assertEqual(self.background.is_conveyor_lift_up, False)

    def test_is_conveyor_lift_down(self):
        self.assertEqual(self.background.is_conveyor_lift_down, True)
