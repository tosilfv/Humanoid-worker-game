import turtle
from random import choice
from utils import constants as const
from utils.helpers import direction_term


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
        self.is_box_pickup = False

    @property
    def box(self):
        """Get box."""
        return self._box

    @property
    def is_box_pickup(self):
        """Get is box pick up boolean value."""
        return self._is_box_pickup

    @is_box_pickup.setter
    def is_box_pickup(self, val):
        """Set is box pick up boolean value."""
        self._is_box_pickup = val

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

    def box_to_left(self, pos, hum_to_right):
        """Move box left."""
        __adjust_x = self.box.xcor()
        __adjust_y = self.box.ycor()
        # Stop at pick up position
        if __adjust_x < pos or __adjust_x < const.BOX_PICKUP_POS_X:
            self.is_box_pickup = True
        else:
            __adjust_x += const.BOX_LEFT_SPEED\
                            + direction_term(hum_to_right, const.ZERO)
            self.box.goto(
                __adjust_x,
                __adjust_y
            )

    def box_pickup(self, pos):
        """Box is at pick up position."""
        self.is_box_pickup = False
        __adjust_x = pos
        __adjust_y = self.box.ycor()
        self.box.goto(
            __adjust_x,
            __adjust_y
        )
