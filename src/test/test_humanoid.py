import unittest
from components import Humanoid


class TestHumanoid(unittest.TestCase):
    """Tests for Humanoid class from components/Humanoid."""

    def setUp(self):
        self.humanoid = Humanoid()

    def test_body_part(self):
        self.assertEqual(len(self.humanoid.body_part), 18)

    def test_move_speed(self):
        self.assertEqual(len(self.humanoid.move_speed), 4)

    def test_left_thigh_heading(self):
        self.assertEqual(self.humanoid.left_thigh_heading, 270)

    def test_left_thigh_extended(self):
        self.assertEqual(self.humanoid.left_thigh_extended, False)

    def test_left_thigh_retracted(self):
        self.assertEqual(self.humanoid.left_thigh_retracted, True)

    def test_right_thigh_heading(self):
        self.assertEqual(self.humanoid.right_thigh_heading, 270)

    def test_right_thigh_extended(self):
        self.assertEqual(self.humanoid.right_thigh_extended, True)

    def test_right_thigh_retracted(self):
        self.assertEqual(self.humanoid.right_thigh_retracted, False)

    def test_humanoid_speed(self):
        self.assertEqual(self.humanoid.humanoid_speed, 0.0001)

    def test_move(self):
        self.assertEqual(self.humanoid.move, False)

    def test_left(self):
        self.assertEqual(self.humanoid.left, False)

    def test_right(self):
        self.assertEqual(self.humanoid.right, True)

    def test_carries_box(self):
        self.assertEqual(self.humanoid.carries_box, False)
