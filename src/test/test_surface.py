import unittest
from components import Surface
from utils.constants import SURFACE_HEADING, SURFACE_POS_X, SURFACE_POS_Y, \
    SQUARE, BLACK, SURFACE_WID, SURFACE_LEN


class TestSurface(unittest.TestCase):
    """Tests for Surface class from components/Surface."""

    def setUp(self):
        self.surface = Surface()

    def test_instance_of_surface(self):
        self.assertIsInstance(self.surface, Surface)

    def test_create_surface_heading(self):
        heading = self.surface.create_surface.heading()
        self.assertEqual(heading, SURFACE_HEADING)

    def test_create_surface_xcor(self):
        loc_x = self.surface.create_surface.xcor()
        self.assertEqual(loc_x, SURFACE_POS_X)

    def test_create_surface_ycor(self):
        loc_y = self.surface.create_surface.ycor()
        self.assertEqual(loc_y, SURFACE_POS_Y)

    def test_create_surface_shape(self):
        shape = self.surface.create_surface.shape()
        self.assertEqual(shape, SQUARE)

    def test_create_surface_color(self):
        color = self.surface.create_surface.pencolor()
        self.assertEqual(color, BLACK)

    def test_create_surface_shapesize(self):
        shapesize = self.surface.create_surface.shapesize()
        self.assertEqual(shapesize, (SURFACE_WID, SURFACE_LEN, 1))
