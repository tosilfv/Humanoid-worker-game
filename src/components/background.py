import turtle
import utils.constants as const
from utils.utils import direction_term

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
        self.__background_empty_mid_pos_x =\
            const.BACKGROUND_EMPTY_MID_POS_X
        self.__background_empty_left_pos_x =\
            const.BACKGROUND_EMPTY_LEFT_POS_X
        self.__background_empty_right_pos_x =\
            const.BACKGROUND_EMPTY_RIGHT_POS_X
        self.__background_light_pos_x =\
            const.BACKGROUND_LIGHT_POS_X
        self.__background_regular_pos_x =\
            const.BACKGROUND_REGULAR_POS_X
        self.__background_heavy_pos_x =\
            const.BACKGROUND_HEAVY_POS_X
        self.__light_lift_pos_y =\
            const.LIGHT_LIFT_POS_Y
        self.__regular_lift_pos_y =\
            const.REGULAR_LIFT_POS_Y
        self.__heavy_lift_pos_y =\
            const.HEAVY_LIFT_POS_Y

        self._background_conveyor_pos_x =\
            const.BACKGROUND_CONVEYOR_POS_X
        self._conveyor_lift_pos_y =\
            const.CONVEYOR_LIFT_POS_Y

        self.light_lift_move = False
        self.regular_lift_move = False
        self.heavy_lift_move = False
        self.conveyor_lift_move = True
        self.trackpoint_to_left = False
        self.timer_to_stop = 0
        self.trackpoint_stop = False
        self.box_is_hoisted = False
        self.box_is_delivered = False
        self.boxes = []
        self.box_index = 0

        # Direction
        self.left = True
        self.right = False
        self.light_lift_up = False
        self.light_lift_down = False
        self.regular_lift_up = False
        self.regular_lift_down = False
        self.heavy_lift_up = False
        self.heavy_lift_down = False
        self.conveyor_lift_up = True
        self.conveyor_lift_down = False

    @property
    def light_lift(self):
        """Get light lift."""
        return self._light_lift

    @property
    def light_lift_xcor(self):
        """Get light lift position x."""
        return self._light_lift.xcor()

    @property
    def regular_lift(self):
        """Get regular lift."""
        return self._regular_lift

    @property
    def regular_lift_xcor(self):
        """Get regular lift position x."""
        return self._regular_lift.xcor()

    @property
    def heavy_lift(self):
        """Get heavy lift."""
        return self._heavy_lift

    @property
    def heavy_lift_xcor(self):
        """Get heavy lift position x."""
        return self._heavy_lift.xcor()

    @property
    def conveyor_drive_xcor(self):
        """Get conveyor drive position x."""
        return self._conveyor_drive.xcor()

    @property
    def conveyor_lift_xcor(self):
        """Get background conveyor lift position x."""
        return self._conveyor_lift.xcor()

    @property
    def conveyor_lift_ycor(self):
        """Get conveyor lift position y."""
        return self._conveyor_lift.ycor()

    @property
    def conveyor_trackpoint(self):
        """Get conveyor trackpoint."""
        return self._conveyor_trackpoint

    def __initialize_background_part(
            self, part, heading, goto_x, goto_y, shape, color, wid, len
            ):
        """Set the background part start properties."""
        self.__background_part[part].penup()
        self.__background_part[part].setheading(heading)
        self.__background_part[part].goto(goto_x, goto_y)
        self.__background_part[part].speed(0)
        self.__background_part[part].shape(shape)
        self.__background_part[part].color(color)
        self.__background_part[part].shapesize(
            stretch_wid=wid,
            stretch_len=len
            )

    def __create_background_empty_mid(self):
        """Creates empty middle background."""
        # Empty middle
        self.__background_empty_mid = turtle.Turtle()
        self.__background_part.update(
            {
                "background_empty_mid": self.__background_empty_mid
            }
        )
        self.__initialize_background_part(
            "background_empty_mid",
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
        self.__background_empty_left = turtle.Turtle()
        self.__background_part.update(
            {
                "background_empty_left": self.__background_empty_left
            }
        )
        self.__initialize_background_part(
            "background_empty_left",
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
        self.__background_empty_right = turtle.Turtle()
        self.__background_part.update(
            {
                "background_empty_right": self.__background_empty_right
            }
        )
        self.__initialize_background_part(
            "background_empty_right",
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
        self.__background_light = turtle.Turtle()
        self.__background_part.update(
            {
                "background_light": self.__background_light
            }
        )
        self.__initialize_background_part(
            "background_light",
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
                "_light_lift": self._light_lift
            }
        )
        self.__initialize_background_part(
            "_light_lift",
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
        self.__background_regular = turtle.Turtle()
        self.__background_part.update(
            {
                "background_regular": self.__background_regular
            }
        )
        self.__initialize_background_part(
            "background_regular",
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
                "_regular_lift": self._regular_lift
            }
        )
        self.__initialize_background_part(
            "_regular_lift",
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
        self.__background_heavy = turtle.Turtle()
        self.__background_part.update(
            {
                "background_heavy": self.__background_heavy
            }
        )
        self.__initialize_background_part(
            "background_heavy",
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
                "_heavy_lift": self._heavy_lift
            }
        )
        self.__initialize_background_part(
            "_heavy_lift",
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
        self.__background_conveyor = turtle.Turtle()
        self.__background_part.update(
            {
                "background_conveyor": self.__background_conveyor
            }
        )
        self.__initialize_background_part(
            "background_conveyor",
            const.BACKGROUND_CONVEYOR_HEADING,
            const.BACKGROUND_CONVEYOR_POS_X,
            const.BACKGROUND_CONVEYOR_POS_Y,
            const.SQUARE,
            const.TROPICALRAINFOREST,
            const.BACKGROUND_CONVEYOR_WID,
            const.BACKGROUND_CONVEYOR_LEN
            )

        # Conveyor belt
        self._conveyor_belt = turtle.Turtle()
        self.__background_part.update(
            {
                "_conveyor_belt": self._conveyor_belt
            }
        )
        self.__initialize_background_part(
            "_conveyor_belt",
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
                "_conveyor_drive": self._conveyor_drive
            }
        )
        self.__initialize_background_part(
            "_conveyor_drive",
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
                "_conveyor_tail": self._conveyor_tail
            }
        )
        self.__initialize_background_part(
            "_conveyor_tail",
            const.CONVEYOR_TAIL_HEADING,
            const.CONVEYOR_TAIL_POS_X,
            const.CONVEYOR_TAIL_POS_Y,
            const.CIRCLE,
            const.FORESTGREEN,
            const.CONVEYOR_TAIL_WID,
            const.CONVEYOR_TAIL_LEN
        )

        # Conveyor lift
        self._conveyor_lift = turtle.Turtle()
        self.__background_part.update(
            {
                "_conveyor_lift": self._conveyor_lift
            }
        )
        self.__initialize_background_part(
            "_conveyor_lift",
            const.CONVEYOR_LIFT_HEADING,
            const.CONVEYOR_LIFT_POS_X,
            const.CONVEYOR_LIFT_POS_Y,
            const.SQUARE,
            const.BLACK,
            const.CONVEYOR_LIFT_WID,
            const.CONVEYOR_LIFT_LEN
        )

        # Conveyor trackpoint
        self._conveyor_trackpoint = turtle.Turtle()
        self.__background_part.update(
            {
                "_conveyor_trackpoint": self._conveyor_trackpoint
            }
        )
        self.__initialize_background_part(
            "_conveyor_trackpoint",
            const.CONVEYOR_TRACKPOINT_HEADING,
            const.CONVEYOR_TRACKPOINT_POS_X,
            const.CONVEYOR_TRACKPOINT_POS_Y,
            const.CIRCLE,
            const.RED,
            const.CONVEYOR_TRACKPOINT_WID,
            const.CONVEYOR_TRACKPOINT_LEN
        )

    def __to_positions(self):
        """Set the position for each background part."""
        self.__background_empty_mid_pos_x +=\
            direction_term(self.left, self.right)
        self.__background_empty_left_pos_x +=\
            direction_term(self.left, self.right)
        self.__background_empty_right_pos_x +=\
            direction_term(self.left, self.right)
        self.__background_light_pos_x +=\
            direction_term(self.left, self.right)
        self.__background_regular_pos_x +=\
            direction_term(self.left, self.right)
        self.__background_heavy_pos_x +=\
            direction_term(self.left, self.right)
        self._background_conveyor_pos_x +=\
            direction_term(self.left, self.right)

        self.__background_empty_mid.goto(
            self.__background_empty_mid_pos_x,
            const.BACKGROUND_EMPTY_MID_POS_Y
            )
        self.__background_empty_left.goto(
            self.__background_empty_left_pos_x,
            const.BACKGROUND_EMPTY_LEFT_POS_Y
            )
        self.__background_empty_right.goto(
            self.__background_empty_right_pos_x,
            const.BACKGROUND_EMPTY_RIGHT_POS_Y
            )
        self.__background_light.goto(
            self.__background_light_pos_x,
            const.BACKGROUND_LIGHT_POS_Y
            )
        self.__background_regular.goto(
            self.__background_regular_pos_x,
            const.BACKGROUND_REGULAR_POS_Y
            )
        self.__background_heavy.goto(
            self.__background_heavy_pos_x,
            const.BACKGROUND_HEAVY_POS_Y
            )
        self.__background_conveyor.goto(
            self._background_conveyor_pos_x,
            const.BACKGROUND_CONVEYOR_POS_Y
            )
        self._light_lift.goto(
            self.__background_light_pos_x + const.LIGHT_LIFT_POS_X,
            self.__light_lift_pos_y
            )
        self._regular_lift.goto(
            self.__background_regular_pos_x + const.REGULAR_LIFT_POS_X,
            self.__regular_lift_pos_y
            )
        self._heavy_lift.goto(
            self.__background_heavy_pos_x + const.HEAVY_LIFT_POS_X,
            self.__heavy_lift_pos_y
            )
        self._conveyor_belt.goto(
            self._background_conveyor_pos_x + const.CONVEYOR_BELT_POS_X,
            const.CONVEYOR_BELT_POS_Y
            )
        self._conveyor_drive.goto(
            self._background_conveyor_pos_x + const.CONVEYOR_DRIVE_POS_X,
            const.CONVEYOR_DRIVE_POS_Y
            )
        self._conveyor_tail.goto(
            self._background_conveyor_pos_x + const.CONVEYOR_TAIL_POS_X,
            const.CONVEYOR_TAIL_POS_Y
            )
        self._conveyor_lift.goto(
            self._background_conveyor_pos_x + const.CONVEYOR_LIFT_POS_X,
            self._conveyor_lift_pos_y
            )

    def __to_start_pos(self):
        """Set background parts to start positions."""        
        self.__background_empty_mid.goto(
            const.BACKGROUND_EMPTY_MID_POS_X,
            const.BACKGROUND_EMPTY_MID_POS_Y
            )
        self.__background_empty_left.goto(
            const.BACKGROUND_EMPTY_LEFT_POS_X,
            const.BACKGROUND_EMPTY_LEFT_POS_Y
            )
        self.__background_empty_right.goto(
            const.BACKGROUND_EMPTY_RIGHT_POS_X,
            const.BACKGROUND_EMPTY_RIGHT_POS_Y
            )
        self.__background_light.goto(
            const.BACKGROUND_LIGHT_POS_X,
            const.BACKGROUND_LIGHT_POS_Y
            )
        self.__background_regular.goto(
            const.BACKGROUND_REGULAR_POS_X,
            const.BACKGROUND_REGULAR_POS_Y
            )
        self.__background_heavy.goto(
            const.BACKGROUND_HEAVY_POS_X,
            const.BACKGROUND_HEAVY_POS_Y
            )
        self.__background_conveyor.goto(
            const.BACKGROUND_CONVEYOR_POS_X,
            const.BACKGROUND_CONVEYOR_POS_Y
            )

    def __to_extreme_pos(self, term):
        """Set background parts to extreme positions."""
        self.__background_empty_mid_pos_x =\
            const.BACKGROUND_EMPTY_MID_POS_X + term
        self.__background_empty_left_pos_x =\
            const.BACKGROUND_EMPTY_LEFT_POS_X + term
        self.__background_empty_right_pos_x =\
            const.BACKGROUND_EMPTY_RIGHT_POS_X + term
        self.__background_light_pos_x =\
            const.BACKGROUND_LIGHT_POS_X + term
        self.__background_regular_pos_x =\
            const.BACKGROUND_REGULAR_POS_X + term
        self.__background_heavy_pos_x =\
            const.BACKGROUND_HEAVY_POS_X + term
        self._background_conveyor_pos_x =\
            const.BACKGROUND_CONVEYOR_POS_X + term

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
        if self.__background_empty_left_pos_x == 0 and self.right:
            self.__to_leftmost_pos()
        elif self.__background_empty_right_pos_x == 0 and self.left:
            self.__to_rightmost_pos()
        else:
            self.__to_positions()

    def update_light_lift(self):
        """Update the position of the light lift."""
        if (self.light_lift_up or self.light_lift_down)\
            and self.__light_lift_pos_y < const.LIGHT_LIFT_MAX_Y + 1:
            self.__light_lift_pos_y +=\
                1 * direction_term(
                    self.light_lift_down,
                    self.light_lift_up
                    )
            self._light_lift.goto(
                self.__background_light_pos_x + const.LIGHT_LIFT_POS_X,
                self.__light_lift_pos_y
            )
        if self.__light_lift_pos_y >= const.LIGHT_LIFT_MAX_Y:
            self.light_lift_up = False
            self.light_lift_down = True
        if self.__light_lift_pos_y <= const.LIGHT_LIFT_MIN_Y:
            self.light_lift_up = False
            self.light_lift_down = False

    def update_regular_lift(self):
        """Update the position of the regular lift."""
        if (self.regular_lift_up or self.regular_lift_down)\
            and self.__regular_lift_pos_y < const.REGULAR_LIFT_MAX_Y + 1:
            self.__regular_lift_pos_y +=\
                1 * direction_term(
                    self.regular_lift_down,
                    self.regular_lift_up
                    )
            self._regular_lift.goto(
                self.__background_regular_pos_x + const.REGULAR_LIFT_POS_X,
                self.__regular_lift_pos_y
            )
        if self.__regular_lift_pos_y >= const.REGULAR_LIFT_MAX_Y:
            self.regular_lift_up = False
            self.regular_lift_down = True
        if self.__regular_lift_pos_y <= const.REGULAR_LIFT_MIN_Y:
            self.regular_lift_up = False
            self.regular_lift_down = False

    def update_heavy_lift(self):
        """Update the position of the heavy lift."""
        if (self.heavy_lift_up or self.heavy_lift_down)\
            and self.__heavy_lift_pos_y < const.HEAVY_LIFT_MAX_Y + 1:
            self.__heavy_lift_pos_y +=\
                1 * direction_term(
                    self.heavy_lift_down,
                    self.heavy_lift_up
                    )
            self._heavy_lift.goto(
                self.__background_heavy_pos_x + const.HEAVY_LIFT_POS_X,
                self.__heavy_lift_pos_y
            )
        if self.__heavy_lift_pos_y >= const.HEAVY_LIFT_MAX_Y:
            self.heavy_lift_up = False
            self.heavy_lift_down = True
        if self.__heavy_lift_pos_y <= const.HEAVY_LIFT_MIN_Y:
            self.heavy_lift_up = False
            self.heavy_lift_down = False

    def update_conveyor_lift(self):
        """Update the position of the conveyor lift."""
        if (self.conveyor_lift_up or self.conveyor_lift_down)\
            and self._conveyor_lift_pos_y < const.CONVEYOR_LIFT_MAX_Y + 1:
            self._conveyor_lift_pos_y +=\
                0.1 * direction_term(
                    self.conveyor_lift_down,
                    self.conveyor_lift_up
                    )
            self._conveyor_lift.goto(
                self._background_conveyor_pos_x + const.CONVEYOR_LIFT_POS_X,
                self._conveyor_lift_pos_y
            )
        if self._conveyor_lift_pos_y >= const.CONVEYOR_LIFT_MAX_Y:
            self.conveyor_lift_up = False
            self.conveyor_lift_down = False
            self.conveyor_lift_move = False
        if self._conveyor_lift_pos_y <= const.CONVEYOR_LIFT_MIN_Y:
            self.conveyor_lift_up = False
            self.conveyor_lift_down = False

    def update_conveyor_trackpoint(self):
        """Update the position of the conveyor trackpoint."""
        self.conveyor_trackpoint.goto(
            self.conveyor_lift_xcor,
            self.conveyor_lift_ycor
            )

    def conveyor_trackpoint_to_left(self):
        """Move the conveyor trackpoint to left."""
        xcor = self.conveyor_trackpoint.xcor()
        xcor -= 1
        self.conveyor_trackpoint.goto(
            xcor,
            self.conveyor_lift_ycor
            )

    def check_if_ready(self):
        """Check if trackpoint is at box pick up position."""
        if self.conveyor_trackpoint.xcor() <=\
            self._background_conveyor_pos_x + const.CONVEYOR_LIFT_POS_X - 500:
            self.trackpoint_to_left = False
