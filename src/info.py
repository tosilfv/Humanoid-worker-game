import turtle
import constants as const

class Info:
    """The information text to show humanoid controls."""


    def __init__(self):
        """Initialize the info components."""
        self.__create_info_text()

    def __create_info_text(self):
        """Creates info text."""
        self.__info = turtle.Turtle()
        self.__info.hideturtle()
        self.__info.penup()
        self.__info.color(const.BLACK)
        self.__info.goto(const.INFO_POS_X, const.INFO_POS_Y)
        self.__info.write(
            "Use Left and Right arrow keys to control humanoid",
            align="center", font=("Arial", 16, "normal")
            )
