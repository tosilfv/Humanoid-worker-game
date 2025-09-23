import turtle
import utils.constants as const
from random import choice

class Box:
    """The box humanoid carries around."""


    def __init__(self):
        """Initialize the box components."""
        self.__box_part = {}
        self.__boxes = [
            self.__create_light_box,
            self.__create_regular_box,
            self.__create_heavy_box
            ]

    @property
    def box(self):
        """Get box."""
        return self._box

    def new_box(self):
        """Creates new random box."""
        choice(self.__boxes)()

    def __initialize_box_part(
            self, part, heading, goto_x, goto_y, shape, color, wid, len
            ):
        """Set the box part start properties."""
        self.__box_part[part].penup()
        self.__box_part[part].setheading(heading)
        self.__box_part[part].goto(goto_x, goto_y)
        self.__box_part[part].speed(const.SPEED)
        self.__box_part[part].shape(shape)
        self.__box_part[part].fillcolor(color)
        self.__box_part[part].shapesize(
            stretch_wid=wid,
            stretch_len=len
            )

    def __create_light_box(self):
        """Creates light box."""
        # Light box
        self.__light_box = turtle.Turtle()
        self.__box_part.update(
            {
                const.NAME_LIGHT_BOX: self.__light_box
            }
        )
        self.__initialize_box_part(
            const.NAME_LIGHT_BOX,
            const.LIGHT_BOX_HEADING,
            const.LIGHT_BOX_POS_X,
            const.LIGHT_BOX_POS_Y,
            const.SQUARE,
            const.BOX_LIGHT_COLOR,
            const.BOX_LIGHT_WID,
            const.BOX_LIGHT_LEN
            )
        self._box = self.__light_box

    def __create_regular_box(self):
        """Creates regular box."""
        # Regular box
        self.__regular_box = turtle.Turtle()
        self.__box_part.update(
            {
                const.NAME_REGULAR_BOX: self.__regular_box
            }
        )
        self.__initialize_box_part(
            const.NAME_REGULAR_BOX,
            const.REGULAR_BOX_HEADING,
            const.REGULAR_BOX_POS_X,
            const.REGULAR_BOX_POS_Y,
            const.SQUARE,
            const.BOX_REGULAR_COLOR,
            const.BOX_REGULAR_WID,
            const.BOX_REGULAR_LEN
            )
        self._box = self.__regular_box

    def __create_heavy_box(self):
        """Creates heavy box."""
        # Heavy box
        self.__heavy_box = turtle.Turtle()
        self.__box_part.update(
            {
                const.NAME_HEAVY_BOX: self.__heavy_box
            }
        )
        self.__initialize_box_part(
            const.NAME_HEAVY_BOX,
            const.HEAVY_BOX_HEADING,
            const.HEAVY_BOX_POS_X,
            const.HEAVY_BOX_POS_Y,
            const.SQUARE,
            const.BOX_HEAVY_COLOR,
            const.BOX_HEAVY_WID,
            const.BOX_HEAVY_LEN
            )
        self._box = self.__heavy_box

    def update_box(self, goto_x, goto_y):
        """Update the position of the box."""
        __adjust_y = const.ADJUST_Y
        if self.box.shapesize() == const.BOX_LIGHT_SHAPESIZE:
            __adjust_y = const.LIGHT_BOX_POS_Y
        elif self.box.shapesize() == const.BOX_REGULAR_SHAPESIZE:
            __adjust_y = const.REGULAR_BOX_POS_Y
        elif self.box.shapesize() == const.BOX_HEAVY_SHAPESIZE:
            __adjust_y = const.HEAVY_BOX_POS_Y
        self.box.goto(
            goto_x,
            goto_y + __adjust_y
            )
