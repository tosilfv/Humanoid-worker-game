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
        """Heavy box will be the self.box, because it's created last.
        To conclude this, you can print the size of heavy box (3, 3, 1) with
        print(self.box.box.shapesize()) inside some of the TestBox methods.
        """
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

    def test_box_part(self):
        self.assertEqual(len(self.box.box_part), 3)

    def test_boxes(self):
        self.assertEqual(len(self.box.boxes), 3)

    def test_is_box_pickup(self):
        self.assertEqual(self.box.is_box_pickup, False)

    def test_box_to_left(self):
        old_xcor = self.box.heavy_box.xcor()
        # To compensate for the effect of background moving left while walking
        # right, the box that is called to go left on the conveyor belt, is
        # shifted by double the amount of the movement pixels. Thus the new
        # x-coordinate of the box should be at -2 instead of -1 of the
        # original position after one call to box_to_left method.
        shift = -2
        walking_right = True
        self.box.box_to_left(old_xcor + shift, walking_right)
        new_xcor = self.box.heavy_box.xcor()
        self.assertEqual(old_xcor + shift, new_xcor)

    def test_box_pickup(self):
        old_xcor = self.box.heavy_box.xcor()
        shift = 1
        self.box.box_pickup(old_xcor + shift)
        new_xcor = self.box.heavy_box.xcor()
        self.assertEqual(old_xcor + shift, new_xcor)

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
