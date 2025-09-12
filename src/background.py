import turtle
import constants as const
from box import Box

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
        self.__background_empty_mid_pos_x = const.BACKGROUND_EMPTY_MID_POS_X
        self.__background_empty_left_pos_x = const.BACKGROUND_EMPTY_LEFT_POS_X
        self.__background_empty_right_pos_x = const.BACKGROUND_EMPTY_RIGHT_POS_X
        self.__background_light_pos_x = const.BACKGROUND_LIGHT_POS_X
        self.__background_regular_pos_x = const.BACKGROUND_REGULAR_POS_X
        self.__background_heavy_pos_x = const.BACKGROUND_HEAVY_POS_X
        self.__background_conveyor_pos_x = const.BACKGROUND_CONVEYOR_POS_X
        self.__conveyor_belt_pos
        self.__conveyor_drive_pos
        self.__conveyor_tail_pos
        self.__conveyor_lift_pos
        self.__light_lift_pos
        self.__regular_lift_pos
        self.__heavy_lift_pos

        # Direction
        self.left = True
        self.right = False

    @property
    def __get_direction_term(self):
        """Return either 1 or -1 depending on background direction."""
        self.__direction_term = (-1 * self.left + self.right)
        return self.__direction_term

    @property
    def __conveyor_belt_pos(self):
        """Return conveyor belt position."""
        return self.__conveyor_belt.setposition(
            self.__background_conveyor_pos_x + const.CONVEYOR_BELT_POS_X,
            const.CONVEYOR_BELT_POS_Y
            )

    @property
    def __conveyor_drive_pos(self):
        """Return conveyor drive position."""
        return self.__conveyor_drive.setposition(
            self.__background_conveyor_pos_x + const.CONVEYOR_DRIVE_POS_X,
            const.CONVEYOR_DRIVE_POS_Y
            )

    @property
    def __conveyor_tail_pos(self):
        """Return conveyor tail position."""
        return self.__conveyor_tail.setposition(
            self.__background_conveyor_pos_x + const.CONVEYOR_TAIL_POS_X,
            const.CONVEYOR_TAIL_POS_Y
            )

    @property
    def __conveyor_lift_pos(self):
        """Return conveyor lift position."""
        return self.__conveyor_lift.setposition(
            self.__background_conveyor_pos_x + const.CONVEYOR_LIFT_POS_X,
            const.CONVEYOR_LIFT_POS_Y
            )

    @property
    def __light_lift_pos(self):
        """Return light lift position."""
        return self.__light_lift.setposition(
            self.__background_light_pos_x + const.LIGHT_LIFT_POS_X,
            const.LIGHT_LIFT_POS_Y
            )

    @property
    def __regular_lift_pos(self):
        """Return regular lift position."""
        return self.__regular_lift.setposition(
            self.__background_regular_pos_x + const.REGULAR_LIFT_POS_X,
            const.REGULAR_LIFT_POS_Y
            )

    @property
    def __heavy_lift_pos(self):
        """Return heavy lift position."""
        return self.__heavy_lift.setposition(
            self.__background_heavy_pos_x + const.HEAVY_LIFT_POS_X,
            const.HEAVY_LIFT_POS_Y
            )

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
        self.__background_part[part].shapesize(stretch_wid=wid, stretch_len=len)

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
        self.__light_lift = turtle.Turtle()
        self.__background_part.update(
            {
                "light_lift": self.__light_lift
            }
        )
        self.__initialize_background_part(
            "light_lift",
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
        self.__regular_lift = turtle.Turtle()
        self.__background_part.update(
            {
                "regular_lift": self.__regular_lift
            }
        )
        self.__initialize_background_part(
            "regular_lift",
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
        self.__heavy_lift = turtle.Turtle()
        self.__background_part.update(
            {
                "heavy_lift": self.__heavy_lift
            }
        )
        self.__initialize_background_part(
            "heavy_lift",
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
        self.__conveyor_belt = turtle.Turtle()
        self.__background_part.update(
            {
                "conveyor_belt": self.__conveyor_belt
            }
        )
        self.__initialize_background_part(
            "conveyor_belt",
            const.CONVEYOR_BELT_HEADING,
            const.CONVEYOR_BELT_POS_X,
            const.CONVEYOR_BELT_POS_Y,
            const.SQUARE,
            const.BLACK,
            const.CONVEYOR_BELT_WID,
            const.CONVEYOR_BELT_LEN
        )

        # Conveyor drive pulley
        self.__conveyor_drive = turtle.Turtle()
        self.__background_part.update(
            {
                "conveyor_drive": self.__conveyor_drive
            }
        )
        self.__initialize_background_part(
            "conveyor_drive",
            const.CONVEYOR_DRIVE_HEADING,
            const.CONVEYOR_DRIVE_POS_X,
            const.CONVEYOR_DRIVE_POS_Y,
            const.CIRCLE,
            const.DARKPASTELGREEN,
            const.CONVEYOR_DRIVE_WID,
            const.CONVEYOR_DRIVE_LEN
        )

        # Conveyor tail pulley
        self.__conveyor_tail = turtle.Turtle()
        self.__background_part.update(
            {
                "conveyor_tail": self.__conveyor_tail
            }
        )
        self.__initialize_background_part(
            "conveyor_tail",
            const.CONVEYOR_TAIL_HEADING,
            const.CONVEYOR_TAIL_POS_X,
            const.CONVEYOR_TAIL_POS_Y,
            const.CIRCLE,
            const.DARKPASTELGREEN,
            const.CONVEYOR_TAIL_WID,
            const.CONVEYOR_TAIL_LEN
        )

        # Conveyor lift
        self.__conveyor_lift = turtle.Turtle()
        self.__background_part.update(
            {
                "conveyor_lift": self.__conveyor_lift
            }
        )
        self.__initialize_background_part(
            "conveyor_lift",
            const.CONVEYOR_LIFT_HEADING,
            const.CONVEYOR_LIFT_POS_X,
            const.CONVEYOR_LIFT_POS_Y,
            const.SQUARE,
            const.BLACK,
            const.CONVEYOR_LIFT_WID,
            const.CONVEYOR_LIFT_LEN
        )

    def __positions(self):
        """Set the position for each backround part."""
        self.__background_empty_mid_pos_x += 1 * self.__get_direction_term
        self.__background_empty_left_pos_x += 1 * self.__get_direction_term
        self.__background_empty_right_pos_x += 1 * self.__get_direction_term
        self.__background_light_pos_x += 1 * self.__get_direction_term
        self.__background_regular_pos_x += 1 * self.__get_direction_term
        self.__background_heavy_pos_x += 1 * self.__get_direction_term
        self.__background_conveyor_pos_x += 1 * self.__get_direction_term
        self.__conveyor_belt_pos
        self.__conveyor_drive_pos
        self.__conveyor_tail_pos
        self.__conveyor_lift_pos
        self.__light_lift_pos
        self.__regular_lift_pos
        self.__heavy_lift_pos

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

    def __to_current_pos(self):
        """Set background parts to current positions."""
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
            self.__background_conveyor_pos_x,
            const.BACKGROUND_CONVEYOR_POS_Y
            )

    def __to_extreme_pos(self, term):
        """Set background parts to extreme positions."""
        self.__background_empty_mid_pos_x = const.BACKGROUND_EMPTY_MID_POS_X\
            + term
        self.__background_empty_left_pos_x = const.BACKGROUND_EMPTY_LEFT_POS_X\
            + term
        self.__background_empty_right_pos_x = const.BACKGROUND_EMPTY_RIGHT_POS_X\
            + term
        self.__background_light_pos_x = const.BACKGROUND_LIGHT_POS_X\
            + term
        self.__background_regular_pos_x = const.BACKGROUND_REGULAR_POS_X\
            + term
        self.__background_heavy_pos_x = const.BACKGROUND_HEAVY_POS_X\
            + term
        self.__background_conveyor_pos_x = const.BACKGROUND_CONVEYOR_POS_X\
            + term

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
            self.__positions()
            self.__to_current_pos()
