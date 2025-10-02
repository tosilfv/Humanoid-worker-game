import turtle
from utils import constants as const


class Info:
    """The information text to show humanoid controls."""

    def __init__(self):
        """Initialize the info components."""
        self.__create_info_text()

    @property
    def create_info_text(self):
        """Get __info turtle object."""
        return self.__info

    def __create_info_text(self):
        """Creates info text."""
        self.__info = turtle.Turtle()
        self.__info.penup()
        self.__info.goto(const.INFO_POS_X, const.INFO_POS_Y)
        self.__info.color(const.BLACK)
        self.__info.hideturtle()
        self.__info.write(
            const.INFO_TEXT,
            align=const.INFO_ALIGN,
            font=(const.FONT_NAME, const.FONT_SIZE, const.FONT_TYPE)
            )
