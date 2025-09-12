import turtle
import constants as const

class Surface:
    """The surface humanoid walks on."""


    def __init__(self):
        """Initialize the surface components."""
        self.__create_surface()

    def __create_surface(self):
        """Creates surface."""
        self.__surface = turtle.Turtle()
        self.__surface.penup()
        self.__surface.setheading(const.SURFACE_HEADING)
        self.__surface.goto(const.SURFACE_POS_X, const.SURFACE_POS_Y)
        self.__surface.speed(0)
        self.__surface.shape(const.SQUARE)
        self.__surface.color(const.BLACK)
        self.__surface.shapesize(
            stretch_wid=const.SURFACE_WID,
            stretch_len=const.SURFACE_LEN
            )
