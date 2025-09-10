import turtle
import constants as const

class Info:
    """The information text to show humanoid controls."""


    def __init__(self):
        """Initialize the info components."""
        self.create_info_text()

    def create_info_text(self):
        """Creates info text."""
        self.info = turtle.Turtle()
        self.info.hideturtle()
        self.info.penup()
        self.info.color(const.BLACK)
        self.info.goto(const.INFO_POS_X, const.INFO_POS_Y)
        self.info.write(
            "Use arrow keys to control humanoid",
            align="center", font=("Arial", 16, "normal")
            )
