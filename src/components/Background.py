import turtle
from utils import constants as const, direction_term


class Background:
    """The background humanoid walks in front of."""

    def __init__(self):
        """Initialize the background components."""
        self.__background_part = {}
        self.__create_background_empty_mid()
        self.__create_background_empty_left()
        self.__create_background_empty_right()
        self.__create_background_light()
        self.__create_background_regular()
        self.__create_background_heavy()
        self.__create_background_conveyor()
        self._left = True
        self._right = False
        self._is_light_lift_up = False
        self._is_light_lift_down = False
        self._is_regular_lift_up = False
        self._is_regular_lift_down = False
        self._is_heavy_lift_up = False
        self._is_heavy_lift_down = False
        self._is_conveyor_lift_up = False
        self._is_conveyor_lift_down = True

    @property
    def left(self):
        """Get left boolean value."""
        return self._left

    @left.setter
    def left(self, is_to_left):
        """Set left boolean value."""
        self._left = is_to_left

    @property
    def right(self):
        """Get right boolean value."""
        return self._right

    @right.setter
    def right(self, is_to_right):
        """Set right boolean value."""
        self._right = is_to_right

    @property
    def background_empty_mid(self):
        """Get background empty mid."""
        return self._background_empty_mid

    @property
    def background_empty_left(self):
        """Get background empty left."""
        return self._background_empty_left

    @property
    def background_empty_right(self):
        """Get background empty right."""
        return self._background_empty_right

    @property
    def background_light(self):
        """Get background light."""
        return self._background_light

    @property
    def background_regular(self):
        """Get background regular."""
        return self._background_regular

    @property
    def background_heavy(self):
        """Get background heavy."""
        return self._background_heavy

    @property
    def background_conveyor(self):
        """Get background conveyor."""
        return self._background_conveyor

    @property
    def light_lift(self):
        """Get light lift."""
        return self._light_lift

    @property
    def regular_lift(self):
        """Get regular lift."""
        return self._regular_lift

    @property
    def heavy_lift(self):
        """Get heavy lift."""
        return self._heavy_lift

    @property
    def conveyor_lift(self):
        """Get conveyor lift."""
        return self._conveyor_lift

    @property
    def conveyor_belt(self):
        """Get conveyor belt."""
        return self._conveyor_belt

    @property
    def conveyor_drive(self):
        """Get conveyor drive."""
        return self._conveyor_drive

    @property
    def conveyor_tail(self):
        """Get conveyor tail."""
        return self._conveyor_tail

    @property
    def trackpoint(self):
        """Get trackpoint."""
        return self._trackpoint

    @property
    def is_light_lift_up(self):
        """Get is light lift up boolean value."""
        return self._is_light_lift_up

    @is_light_lift_up.setter
    def is_light_lift_up(self, val):
        """Set is light lift up boolean value."""
        self._is_light_lift_up = val

    @property
    def is_light_lift_down(self):
        """Get is light lift down boolean value."""
        return self._is_light_lift_down

    @is_light_lift_down.setter
    def is_light_lift_down(self, val):
        """Set is light lift down boolean value."""
        self._is_light_lift_down = val

    @property
    def is_regular_lift_up(self):
        """Get is regular lift up boolean value."""
        return self._is_regular_lift_up

    @is_regular_lift_up.setter
    def is_regular_lift_up(self, val):
        """Set is regular lift up boolean value."""
        self._is_regular_lift_up = val

    @property
    def is_regular_lift_down(self):
        """Get is regular lift down boolean value."""
        return self._is_regular_lift_down

    @is_regular_lift_down.setter
    def is_regular_lift_down(self, val):
        """Set is regular lift down boolean value."""
        self._is_regular_lift_down = val

    @property
    def is_heavy_lift_up(self):
        """Get is heavy lift up boolean value."""
        return self._is_heavy_lift_up

    @is_heavy_lift_up.setter
    def is_heavy_lift_up(self, val):
        """Set is heavy lift up boolean value."""
        self._is_heavy_lift_up = val

    @property
    def is_heavy_lift_down(self):
        """Get is heavy lift down boolean value."""
        return self._is_heavy_lift_down

    @is_heavy_lift_down.setter
    def is_heavy_lift_down(self, val):
        """Set is heavy lift down boolean value."""
        self._is_heavy_lift_down = val

    @property
    def is_conveyor_lift_up(self):
        """Get is conveyor lift up boolean value."""
        return self._is_conveyor_lift_up

    @is_conveyor_lift_up.setter
    def is_conveyor_lift_up(self, val):
        """Set is conveyor lift up boolean value."""
        self._is_conveyor_lift_up = val

    @property
    def is_conveyor_lift_down(self):
        """Get is conveyor lift down boolean value."""
        return self._is_conveyor_lift_down

    @is_conveyor_lift_down.setter
    def is_conveyor_lift_down(self, val):
        """Set is conveyor lift down boolean value."""
        self._is_conveyor_lift_down = val

    def __initialize_background_part(
            self, part, heading, goto_x, goto_y, shape, color, wid, len
            ):
        """Set the background part start properties."""
        self.__background_part[part].penup()
        self.__background_part[part].setheading(heading)
        self.__background_part[part].goto(goto_x, goto_y)
        self.__background_part[part].speed(const.SPEED)
        self.__background_part[part].shape(shape)
        self.__background_part[part].color(color)
        self.__background_part[part].shapesize(
            stretch_wid=wid,
            stretch_len=len
            )

    def __create_background_empty_mid(self):
        """Creates empty middle background."""
        # Empty middle
        self._background_empty_mid = turtle.Turtle()
        self.__background_part.update(
            {
                const.BACKGROUND_EMPTY_MID_NAME: self._background_empty_mid
            }
        )
        self.__initialize_background_part(
            const.BACKGROUND_EMPTY_MID_NAME,
            const.BACKGROUND_EMPTY_MID_HEADING,
            const.BACKGROUND_EMPTY_MID_POS_X,
            const.BACKGROUND_EMPTY_MID_POS_Y,
            const.SQUARE,
            const.DAYSKYBLUE,
            const.BACKGROUND_EMPTY_MID_WID,
            const.BACKGROUND_EMPTY_MID_LEN
            )

    def __create_background_empty_left(self):
        """Creates empty left hand side background."""
        # Empty left
        self._background_empty_left = turtle.Turtle()
        self.__background_part.update(
            {
                const.BACKGROUND_EMPTY_LEFT_NAME: self._background_empty_left
            }
        )
        self.__initialize_background_part(
            const.BACKGROUND_EMPTY_LEFT_NAME,
            const.BACKGROUND_EMPTY_LEFT_HEADING,
            const.BACKGROUND_EMPTY_LEFT_POS_X,
            const.BACKGROUND_EMPTY_LEFT_POS_Y,
            const.SQUARE,
            const.DAYSKYBLUE,
            const.BACKGROUND_EMPTY_LEFT_WID,
            const.BACKGROUND_EMPTY_LEFT_LEN
            )

    def __create_background_empty_right(self):
        """Creates empty right hand side background."""
        # Empty right
        self._background_empty_right = turtle.Turtle()
        self.__background_part.update(
            {
                const.BACKGROUND_EMPTY_RIGHT_NAME: self._background_empty_right
            }
        )
        self.__initialize_background_part(
            const.BACKGROUND_EMPTY_RIGHT_NAME,
            const.BACKGROUND_EMPTY_RIGHT_HEADING,
            const.BACKGROUND_EMPTY_RIGHT_POS_X,
            const.BACKGROUND_EMPTY_RIGHT_POS_Y,
            const.SQUARE,
            const.DAYSKYBLUE,
            const.BACKGROUND_EMPTY_RIGHT_WID,
            const.BACKGROUND_EMPTY_RIGHT_LEN
            )

    def __create_background_light(self):
        """Creates light goods storage background."""
        # Light goods storage
        self._background_light = turtle.Turtle()
        self.__background_part.update(
            {
                const.BACKGROUND_LIGHT_NAME: self._background_light
            }
        )
        self.__initialize_background_part(
            const.BACKGROUND_LIGHT_NAME,
            const.BACKGROUND_LIGHT_HEADING,
            const.BACKGROUND_LIGHT_POS_X,
            const.BACKGROUND_LIGHT_POS_Y,
            const.SQUARE,
            const.BLEACHEDDENIM,
            const.BACKGROUND_LIGHT_WID,
            const.BACKGROUND_LIGHT_LEN
            )

        # Light lift
        self._light_lift = turtle.Turtle()
        self.__background_part.update(
            {
                const.LIGHT_LIFT_NAME: self._light_lift
            }
        )
        self.__initialize_background_part(
            const.LIGHT_LIFT_NAME,
            const.LIGHT_LIFT_HEADING,
            const.LIGHT_LIFT_POS_X,
            const.LIGHT_LIFT_POS_Y,
            const.SQUARE,
            const.BLACK,
            const.LIGHT_LIFT_WID,
            const.LIGHT_LIFT_LEN
        )

    def __create_background_regular(self):
        """Creates regular goods storage background."""
        # Regular goods storage
        self._background_regular = turtle.Turtle()
        self.__background_part.update(
            {
                const.BACKGROUND_REGULAR_NAME: self._background_regular
            }
        )
        self.__initialize_background_part(
            const.BACKGROUND_REGULAR_NAME,
            const.BACKGROUND_REGULAR_HEADING,
            const.BACKGROUND_REGULAR_POS_X,
            const.BACKGROUND_REGULAR_POS_Y,
            const.SQUARE,
            const.OCEANDENIM,
            const.BACKGROUND_REGULAR_WID,
            const.BACKGROUND_REGULAR_LEN
            )

        # Regular lift
        self._regular_lift = turtle.Turtle()
        self.__background_part.update(
            {
                const.REGULAR_LIFT_NAME: self._regular_lift
            }
        )
        self.__initialize_background_part(
            const.REGULAR_LIFT_NAME,
            const.REGULAR_LIFT_HEADING,
            const.REGULAR_LIFT_POS_X,
            const.REGULAR_LIFT_POS_Y,
            const.SQUARE,
            const.BLACK,
            const.REGULAR_LIFT_WID,
            const.REGULAR_LIFT_LEN
        )

    def __create_background_heavy(self):
        """Creates heavy goods storage background."""
        # Heavy goods storage
        self._background_heavy = turtle.Turtle()
        self.__background_part.update(
            {
                const.BACKGROUND_HEAVY_NAME: self._background_heavy
            }
        )
        self.__initialize_background_part(
            const.BACKGROUND_HEAVY_NAME,
            const.BACKGROUND_HEAVY_HEADING,
            const.BACKGROUND_HEAVY_POS_X,
            const.BACKGROUND_HEAVY_POS_Y,
            const.SQUARE,
            const.MIDNIGHTDENIM,
            const.BACKGROUND_HEAVY_WID,
            const.BACKGROUND_HEAVY_LEN
            )

        # Heavy lift
        self._heavy_lift = turtle.Turtle()
        self.__background_part.update(
            {
                const.HEAVY_LIFT_NAME: self._heavy_lift
            }
        )
        self.__initialize_background_part(
            const.HEAVY_LIFT_NAME,
            const.HEAVY_LIFT_HEADING,
            const.HEAVY_LIFT_POS_X,
            const.HEAVY_LIFT_POS_Y,
            const.SQUARE,
            const.BLACK,
            const.HEAVY_LIFT_WID,
            const.HEAVY_LIFT_LEN
        )

    def __create_background_conveyor(self):
        """Creates goods conveyor background."""
        # Conveyor background
        self._background_conveyor = turtle.Turtle()
        self.__background_part.update(
            {
                const.BACKGROUND_CONVEYOR_NAME: self._background_conveyor
            }
        )
        self.__initialize_background_part(
            const.BACKGROUND_CONVEYOR_NAME,
            const.BACKGROUND_CONVEYOR_HEADING,
            const.BACKGROUND_CONVEYOR_POS_X,
            const.BACKGROUND_CONVEYOR_POS_Y,
            const.SQUARE,
            const.TROPICALRAINFOREST,
            const.BACKGROUND_CONVEYOR_WID,
            const.BACKGROUND_CONVEYOR_LEN
            )

        # Conveyor lift
        self._conveyor_lift = turtle.Turtle()
        self.__background_part.update(
            {
                const.CONVEYOR_LIFT_NAME: self._conveyor_lift
            }
        )
        self.__initialize_background_part(
            const.CONVEYOR_LIFT_NAME,
            const.CONVEYOR_LIFT_HEADING,
            const.CONVEYOR_LIFT_POS_X,
            const.CONVEYOR_LIFT_POS_Y,
            const.SQUARE,
            const.BLACK,
            const.CONVEYOR_LIFT_WID,
            const.CONVEYOR_LIFT_LEN
        )

        # Conveyor belt
        self._conveyor_belt = turtle.Turtle()
        self.__background_part.update(
            {
                const.CONVEYOR_BELT_NAME: self._conveyor_belt
            }
        )
        self.__initialize_background_part(
            const.CONVEYOR_BELT_NAME,
            const.CONVEYOR_BELT_HEADING,
            const.CONVEYOR_BELT_POS_X,
            const.CONVEYOR_BELT_POS_Y,
            const.SQUARE,
            const.BLACK,
            const.CONVEYOR_BELT_WID,
            const.CONVEYOR_BELT_LEN
        )

        # Conveyor drive pulley
        self._conveyor_drive = turtle.Turtle()
        self.__background_part.update(
            {
                const.CONVEYOR_DRIVE_NAME: self._conveyor_drive
            }
        )
        self.__initialize_background_part(
            const.CONVEYOR_DRIVE_NAME,
            const.CONVEYOR_DRIVE_HEADING,
            const.CONVEYOR_DRIVE_POS_X,
            const.CONVEYOR_DRIVE_POS_Y,
            const.CIRCLE,
            const.FORESTGREEN,
            const.CONVEYOR_DRIVE_WID,
            const.CONVEYOR_DRIVE_LEN
        )

        # Conveyor tail pulley
        self._conveyor_tail = turtle.Turtle()
        self.__background_part.update(
            {
                const.CONVEYOR_TAIL_NAME: self._conveyor_tail
            }
        )
        self.__initialize_background_part(
            const.CONVEYOR_TAIL_NAME,
            const.CONVEYOR_TAIL_HEADING,
            const.CONVEYOR_TAIL_POS_X,
            const.CONVEYOR_TAIL_POS_Y,
            const.CIRCLE,
            const.FORESTGREEN,
            const.CONVEYOR_TAIL_WID,
            const.CONVEYOR_TAIL_LEN
        )

    def __to_positions(self):
        """Set the position for each background part."""
        __term = direction_term(self.left, self.right)

        self.background_empty_mid.goto(
            self.background_empty_mid.xcor() + __term,
            const.BACKGROUND_EMPTY_MID_POS_Y
            )
        self.background_empty_left.goto(
            self.background_empty_left.xcor() + __term,
            const.BACKGROUND_EMPTY_LEFT_POS_Y
            )
        self.background_empty_right.goto(
            self.background_empty_right.xcor() + __term,
            const.BACKGROUND_EMPTY_RIGHT_POS_Y
            )
        self.background_light.goto(
            self.background_light.xcor() + __term,
            const.BACKGROUND_LIGHT_POS_Y
            )
        self.background_regular.goto(
            self.background_regular.xcor() + __term,
            const.BACKGROUND_REGULAR_POS_Y
            )
        self.background_heavy.goto(
            self.background_heavy.xcor() + __term,
            const.BACKGROUND_HEAVY_POS_Y
            )
        self.background_conveyor.goto(
            self.background_conveyor.xcor() + __term,
            const.BACKGROUND_CONVEYOR_POS_Y
            )
        self.light_lift.goto(
            self._background_light.xcor() + const.LIGHT_LIFT_POS_X,
            self.light_lift.ycor()
            )
        self.regular_lift.goto(
            self.background_regular.xcor() + const.REGULAR_LIFT_POS_X,
            self.regular_lift.ycor()
            )
        self.heavy_lift.goto(
            self.background_heavy.xcor() + const.HEAVY_LIFT_POS_X,
            self.heavy_lift.ycor()
            )
        self.conveyor_lift.goto(
            self.background_conveyor.xcor() + const.CONVEYOR_LIFT_POS_X\
                + __term,
            self.conveyor_lift.ycor()
            )
        self.conveyor_belt.goto(
            self.background_conveyor.xcor() + const.CONVEYOR_BELT_POS_X\
                + __term,
            const.CONVEYOR_BELT_POS_Y
            )
        self.conveyor_drive.goto(
            self.background_conveyor.xcor() + const.CONVEYOR_DRIVE_POS_X\
                + __term,
            const.CONVEYOR_DRIVE_POS_Y
            )
        self.conveyor_tail.goto(
            self.background_conveyor.xcor() + const.CONVEYOR_TAIL_POS_X\
                + __term,
            const.CONVEYOR_TAIL_POS_Y
            )

    def __to_start_pos(self):
        """Set background parts to start positions."""        
        self.background_empty_mid.goto(
            const.BACKGROUND_EMPTY_MID_POS_X,
            const.BACKGROUND_EMPTY_MID_POS_Y
            )
        self.background_empty_left.goto(
            const.BACKGROUND_EMPTY_LEFT_POS_X,
            const.BACKGROUND_EMPTY_LEFT_POS_Y
            )
        self.background_empty_right.goto(
            const.BACKGROUND_EMPTY_RIGHT_POS_X,
            const.BACKGROUND_EMPTY_RIGHT_POS_Y
            )
        self.background_light.goto(
            const.BACKGROUND_LIGHT_POS_X,
            const.BACKGROUND_LIGHT_POS_Y
            )
        self.background_regular.goto(
            const.BACKGROUND_REGULAR_POS_X,
            const.BACKGROUND_REGULAR_POS_Y
            )
        self.background_heavy.goto(
            const.BACKGROUND_HEAVY_POS_X,
            const.BACKGROUND_HEAVY_POS_Y
            )
        self.background_conveyor.goto(
            const.BACKGROUND_CONVEYOR_POS_X,
            const.BACKGROUND_CONVEYOR_POS_Y
            )

    def __to_extreme_pos(self, term):
        """Set background parts to extreme positions."""
        self.background_empty_mid.goto(
            const.BACKGROUND_EMPTY_MID_POS_X + term,
            self.background_empty_mid.ycor()
        )
        self.background_empty_left.goto(
            const.BACKGROUND_EMPTY_LEFT_POS_X + term,
            self.background_empty_left.ycor()
        )
        self.background_empty_right.goto(
            const.BACKGROUND_EMPTY_RIGHT_POS_X + term,
            self.background_empty_right.ycor()
        )
        self.background_light.goto(
            const.BACKGROUND_LIGHT_POS_X + term,
            self.background_light.ycor()
        )
        self.background_regular.goto(
            const.BACKGROUND_REGULAR_POS_X + term,
            self.background_regular.ycor()
        )
        self.background_heavy.goto(
            const.BACKGROUND_HEAVY_POS_X + term,
            self.background_heavy.ycor()
        )
        self.background_conveyor.goto(
            const.BACKGROUND_CONVEYOR_POS_X + term,
            self.background_conveyor.ycor()
        )

    def __to_leftmost_pos(self):
        """Set background parts to leftmost position."""
        self.__to_start_pos()
        self.__to_extreme_pos(const.LEFTMOST_TERM)

    def __to_rightmost_pos(self):
        """Set background parts to rightmost position."""
        self.__to_start_pos()
        self.__to_extreme_pos(const.RIGHTMOST_TERM)

    def update_background(self):
        """Update the position of the background."""
        if self.background_empty_left.xcor() == 0 and self.right:
            self.__to_leftmost_pos()
        elif self.background_empty_right.xcor() == 0 and self.left:
            self.__to_rightmost_pos()
        else:
            self.__to_positions()

    def light_lift_to_up(self):
        """Move light lift up."""
        __adjust_x = self.background_light.xcor()\
                        + const.LIGHT_LIFT_POS_X
        __adjust_y = self.light_lift.ycor()
        # Stop at top position
        if __adjust_y >= const.LIGHT_LIFT_MAX_Y:
            self.is_light_lift_up = True
            self.is_light_lift_down = False
        else:
            __adjust_y += const.LIGHT_LIFT_SPEED
            self.light_lift.goto(
                __adjust_x,
                __adjust_y
            )
            self.is_light_lift_up = False
            self.is_light_lift_down = False

    def light_lift_to_down(self):
        """Move light lift down."""
        __adjust_x = self.background_light.xcor()\
                        + const.LIGHT_LIFT_POS_X
        __adjust_y = self.light_lift.ycor()
        # Stop at down position
        if __adjust_y <= const.LIGHT_LIFT_MIN_Y:
            self.is_light_lift_up = False
            self.is_light_lift_down = True
        else:
            __adjust_y -= const.LIGHT_LIFT_SPEED
            self.light_lift.goto(
                __adjust_x,
                __adjust_y
            )
            self.is_light_lift_up = False
            self.is_light_lift_down = False

    def regular_lift_to_up(self):
        """Move regular lift up."""
        __adjust_x = self.background_regular.xcor()\
                        + const.REGULAR_LIFT_POS_X
        __adjust_y = self.regular_lift.ycor()
        # Stop at top position
        if __adjust_y >= const.REGULAR_LIFT_MAX_Y:
            self.is_regular_lift_up = True
            self.is_regular_lift_down = False
        else:
            __adjust_y += const.REGULAR_LIFT_SPEED
            self.regular_lift.goto(
                __adjust_x,
                __adjust_y
            )
            self.is_regular_lift_up = False
            self.is_regular_lift_down = False

    def regular_lift_to_down(self):
        """Move regular lift down."""
        __adjust_x = self.background_regular.xcor()\
                        + const.REGULAR_LIFT_POS_X
        __adjust_y = self.regular_lift.ycor()
        # Stop at down position
        if __adjust_y <= const.REGULAR_LIFT_MIN_Y:
            self.is_regular_lift_up = False
            self.is_regular_lift_down = True
        else:
            __adjust_y -= const.REGULAR_LIFT_SPEED
            self.regular_lift.goto(
                __adjust_x,
                __adjust_y
            )
            self.is_regular_lift_up = False
            self.is_regular_lift_down = False

    def heavy_lift_to_up(self):
        """Move heavy lift up."""
        __adjust_x = self.background_heavy.xcor()\
                        + const.HEAVY_LIFT_POS_X
        __adjust_y = self.heavy_lift.ycor()
        # Stop at top position
        if __adjust_y >= const.HEAVY_LIFT_MAX_Y:
            self.is_heavy_lift_up = True
            self.is_heavy_lift_down = False
        else:
            __adjust_y += const.HEAVY_LIFT_SPEED
            self.heavy_lift.goto(
                __adjust_x,
                __adjust_y
            )
            self.is_heavy_lift_up = False
            self.is_heavy_lift_down = False

    def heavy_lift_to_down(self):
        """Move heavy lift down."""
        __adjust_x = self.background_heavy.xcor()\
                        + const.HEAVY_LIFT_POS_X
        __adjust_y = self.heavy_lift.ycor()
        # Stop at down position
        if __adjust_y <= const.HEAVY_LIFT_MIN_Y:
            self.is_heavy_lift_up = False
            self.is_heavy_lift_down = True
        else:
            __adjust_y -= const.HEAVY_LIFT_SPEED
            self.heavy_lift.goto(
                __adjust_x,
                __adjust_y
            )
            self.is_heavy_lift_up = False
            self.is_heavy_lift_down = False

    def conveyor_lift_to_up(self):
        """Move conveyor lift up."""
        __adjust_x = self.background_conveyor.xcor()\
                        + const.CONVEYOR_LIFT_POS_X
        __adjust_y = self.conveyor_lift.ycor()
        # Stop at top position
        if __adjust_y >= const.CONVEYOR_LIFT_MAX_Y:
            self.is_conveyor_lift_up = True
            self.is_conveyor_lift_down = False
        else:
            __adjust_y += const.CONVEYOR_LIFT_SPEED
            self.conveyor_lift.goto(
                __adjust_x,
                __adjust_y
            )
            self.is_conveyor_lift_up = False
            self.is_conveyor_lift_down = False

    def conveyor_lift_to_down(self):
        """Move conveyor lift down."""
        __adjust_x = self.background_conveyor.xcor()\
                        + const.CONVEYOR_LIFT_POS_X
        __adjust_y = self.conveyor_lift.ycor()
        # Stop at down position
        if __adjust_y <= const.CONVEYOR_LIFT_MIN_Y:
            self.is_conveyor_lift_up = False
            self.is_conveyor_lift_down = True
        else:
            __adjust_y -= const.CONVEYOR_LIFT_SPEED
            self.conveyor_lift.goto(
                __adjust_x,
                __adjust_y
            )
            self.is_conveyor_lift_up = False
            self.is_conveyor_lift_down = False
