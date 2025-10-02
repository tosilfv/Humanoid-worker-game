import unittest
from components import Box
from utils.constants import \
    LIGHT_BOX_HEADING, LIGHT_BOX_POS_X, LIGHT_BOX_POS_Y, \
    SQUARE, BOX_LIGHT_COLOR, BOX_LIGHT_WID, BOX_LIGHT_LEN, \
    REGULAR_BOX_HEADING, REGULAR_BOX_POS_X, REGULAR_BOX_POS_Y, \
    BOX_REGULAR_COLOR, BOX_REGULAR_WID, BOX_REGULAR_LEN, \
    HEAVY_BOX_HEADING, HEAVY_BOX_POS_X, HEAVY_BOX_POS_Y, \
    BOX_HEAVY_COLOR, BOX_HEAVY_WID, BOX_HEAVY_LEN


class TestBox(unittest.TestCase):
    """Tests for Box class from components/Box."""

    def setUp(self):
        self.box = Box()
        self.box.create_light_box()
        self.box.create_regular_box()
        self.box.create_heavy_box()

    def rgb_to_hex(self, color):
        r, g, b = color
        return (
                '#{:02x}{:02x}{:02x}'\
                    .format(int(r * 255), int(g * 255), int(b * 255)))\
                        .upper()

    def test_instance_of_box(self):
        self.assertIsInstance(self.box, Box)

    # Light box
    def test_create_light_box_heading(self):
        heading = self.box.light_box.heading()
        self.assertEqual(heading, LIGHT_BOX_HEADING)

    def test_create_light_box_xcor(self):
        loc_x = self.box.light_box.xcor()
        self.assertEqual(loc_x, LIGHT_BOX_POS_X)

    def test_create_light_box_ycor(self):
        loc_y = self.box.light_box.ycor()
        self.assertEqual(loc_y, LIGHT_BOX_POS_Y)

    def test_create_light_box_shape(self):
        shape = self.box.light_box.shape()
        self.assertEqual(shape, SQUARE)

    def test_create_light_box_color(self):
        color = self.rgb_to_hex(self.box.light_box.fillcolor())
        self.assertEqual(color, BOX_LIGHT_COLOR)

    def test_create_light_box_shapesize(self):
        shapesize = self.box.light_box.shapesize()
        self.assertEqual(shapesize, (BOX_LIGHT_WID, BOX_LIGHT_LEN, 1))

    # Regular box
    def test_create_regular_box_heading(self):
        heading = self.box.regular_box.heading()
        self.assertEqual(heading, REGULAR_BOX_HEADING)

    def test_create_regular_box_xcor(self):
        loc_x = self.box.regular_box.xcor()
        self.assertEqual(loc_x, REGULAR_BOX_POS_X)

    def test_create_regular_box_ycor(self):
        loc_y = self.box.regular_box.ycor()
        self.assertEqual(loc_y, REGULAR_BOX_POS_Y)

    def test_create_regular_box_shape(self):
        shape = self.box.regular_box.shape()
        self.assertEqual(shape, SQUARE)

    def test_create_regular_box_color(self):
        color = self.rgb_to_hex(self.box.regular_box.fillcolor())
        self.assertEqual(color, BOX_REGULAR_COLOR)

    def test_create_regular_box_shapesize(self):
        shapesize = self.box.regular_box.shapesize()
        self.assertEqual(shapesize, (BOX_REGULAR_WID, BOX_REGULAR_LEN, 1))

    # Heavy box
    def test_create_heavy_box_heading(self):
        heading = self.box.heavy_box.heading()
        self.assertEqual(heading, HEAVY_BOX_HEADING)

    def test_create_heavy_box_xcor(self):
        loc_x = self.box.heavy_box.xcor()
        self.assertEqual(loc_x, HEAVY_BOX_POS_X)

    def test_create_heavy_box_ycor(self):
        loc_y = self.box.heavy_box.ycor()
        self.assertEqual(loc_y, HEAVY_BOX_POS_Y)

    def test_create_heavy_box_shape(self):
        shape = self.box.heavy_box.shape()
        self.assertEqual(shape, SQUARE)

    def test_create_heavy_box_color(self):
        color = self.rgb_to_hex(self.box.heavy_box.fillcolor())
        self.assertEqual(color, BOX_HEAVY_COLOR)

    def test_create_heavy_box_shapesize(self):
        shapesize = self.box.heavy_box.shapesize()
        self.assertEqual(shapesize, (BOX_HEAVY_WID, BOX_HEAVY_LEN, 1))
