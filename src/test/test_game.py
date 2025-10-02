import unittest
from control import Game


class TestGame(unittest.TestCase):
    """Tests for Game class from control/Game."""

    def setUp(self):
        self.game = Game()

    def test_box_carry_positions(self):
        self.assertEqual(len(self.game.box_carry_positions), 3)

    def test_box_transport_positions(self):
        self.assertEqual(len(self.game.box_transport_positions), 3)

    def test_box_shape(self):
        self.assertEqual(self.game.box_shape, "")

    def test_box_carry_pos_x(self):
        self.assertEqual(self.game.box_carry_pos_x, 0)

    def test_box_carry_pos_y(self):
        self.assertEqual(self.game.box_carry_pos_y, 0)

    def test_box_trans_pos_x(self):
        self.assertEqual(self.game.box_trans_pos_x, 0)

    def test_box_trans_pos_y(self):
        self.assertEqual(self.game.box_trans_pos_y, 0)

    def test_boxes(self):
        self.assertEqual(self.game.boxes, [])

    def test_box_index(self):
        self.assertEqual(self.game.box_index, -1)

    def test_exit_message(self):
        self.assertEqual(self.game.exit_message, "Thanks for playing!")

    def test_game_on(self):
        self.assertEqual(self.game.game_on, False)

    def test_create_box(self):
        self.assertEqual(self.game.create_box, False)

    def test_created_box(self):
        self.assertEqual(self.game.created_box, False)

    def test_light_lift_up(self):
        self.assertEqual(self.game.light_lift_up, False)

    def test_light_lift_down(self):
        self.assertEqual(self.game.light_lift_down, False)

    def test_regular_lift_up(self):
        self.assertEqual(self.game.regular_lift_up, False)

    def test_regular_lift_down(self):
        self.assertEqual(self.game.regular_lift_down, False)

    def test_heavy_lift_up(self):
        self.assertEqual(self.game.heavy_lift_up, False)

    def test_heavy_lift_down(self):
        self.assertEqual(self.game.heavy_lift_down, False)

    def test_conveyor_lift_up(self):
        self.assertEqual(self.game.conveyor_lift_up, False)

    def test_conveyor_lift_down(self):
        self.assertEqual(self.game.conveyor_lift_down, False)

    def test_box_left(self):
        self.assertEqual(self.game.box_left, False)

    def test_ready_pickup(self):
        self.assertEqual(self.game.ready_pickup, False)

    def test_carrying_box(self):
        self.assertEqual(self.game.carrying_box, False)

    def test_box_in_light_lift(self):
        self.assertEqual(self.game.box_in_light_lift, False)

    def test_box_in_regular_lift(self):
        self.assertEqual(self.game.box_in_regular_lift, False)

    def test_box_in_heavy_lift(self):
        self.assertEqual(self.game.box_in_heavy_lift, False)
