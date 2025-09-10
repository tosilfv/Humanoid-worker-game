import turtle
import constants as const

class Surface:
    """The surface humanoid walks on."""


    def __init__(self):
        """Initialize the surface components."""
        self.create_surface()

    def create_surface(self):
        """Creates surface."""
        self.surface = turtle.Turtle()
        self.surface.penup()
        self.surface.setheading(const.SURFACE_HEADING)
        self.surface.goto(const.SURFACE_POS_X, const.SURFACE_POS_Y)
        self.surface.speed(0)
        self.surface.shape(const.SQUARE)
        self.surface.color(const.BLACK)
        self.surface.shapesize(
            stretch_wid=const.SURFACE_WID,
            stretch_len=const.SURFACE_LEN
            )
