import turtle
import constants as const

class Background:
    """The background humanoid walks in front of."""


    def __init__(self):
        """Initialize the background components."""
        self.background_part = {}
        self.create_background_empty_mid()
        self.create_background_empty_left()
        self.create_background_empty_right()
        self.create_background_light()
        self.create_background_regular()
        self.create_background_heavy()
        self.create_background_conveyor()
        self.background_empty_mid_pos_x = const.BACKGROUND_EMPTY_MID_POS_X
        self.background_empty_left_pos_x = const.BACKGROUND_EMPTY_LEFT_POS_X
        self.background_empty_right_pos_x = const.BACKGROUND_EMPTY_RIGHT_POS_X
        self.background_light_pos_x = const.BACKGROUND_LIGHT_POS_X
        self.background_regular_pos_x = const.BACKGROUND_REGULAR_POS_X
        self.background_heavy_pos_x = const.BACKGROUND_HEAVY_POS_X
        self.background_conveyor_pos_x = const.BACKGROUND_CONVEYOR_POS_X

        # Direction
        self.left = True
        self.right = False

    @property
    def direction_term(self):
        """Return either 1 or -1 depending on background direction."""
        self._direction_term = (-1 * self.left + self.right)
        return self._direction_term

    def initialize_background_part(
            self, part, heading, goto_x, goto_y, shape, color, wid, len
            ):
        """Set the background part start properties."""
        self.background_part[part].penup()
        self.background_part[part].setheading(heading)
        self.background_part[part].goto(goto_x, goto_y)
        self.background_part[part].speed(0)
        self.background_part[part].shape(shape)
        self.background_part[part].color(color)
        self.background_part[part].shapesize(stretch_wid=wid, stretch_len=len)

    def create_background_empty_mid(self):
        """Creates empty middle background."""
        # Empty middle
        self.background_empty_mid = turtle.Turtle()
        self.background_part.update(
            {
                "background_empty_mid": self.background_empty_mid
            }
        )
        self.initialize_background_part(
            "background_empty_mid",
            const.BACKGROUND_EMPTY_MID_HEADING,
            const.BACKGROUND_EMPTY_MID_POS_X,
            const.BACKGROUND_EMPTY_MID_POS_Y,
            const.SQUARE, const.CLASSICDENIM,
            const.BACKGROUND_EMPTY_MID_WID,
            const.BACKGROUND_EMPTY_MID_LEN
            )

    def create_background_empty_left(self):
        """Creates empty left hand side background."""
        # Empty left
        self.background_empty_left = turtle.Turtle()
        self.background_part.update(
            {
                "background_empty_left": self.background_empty_left
            }
        )
        self.initialize_background_part(
            "background_empty_left",
            const.BACKGROUND_EMPTY_LEFT_HEADING,
            const.BACKGROUND_EMPTY_LEFT_POS_X,
            const.BACKGROUND_EMPTY_LEFT_POS_Y,
            const.SQUARE,
            const.CLASSICDENIM,
            const.BACKGROUND_EMPTY_LEFT_WID,
            const.BACKGROUND_EMPTY_LEFT_LEN
            )

    def create_background_empty_right(self):
        """Creates empty right hand side background."""
        # Empty right
        self.background_empty_right = turtle.Turtle()
        self.background_part.update(
            {
                "background_empty_right": self.background_empty_right
            }
        )
        self.initialize_background_part(
            "background_empty_right",
            const.BACKGROUND_EMPTY_RIGHT_HEADING,
            const.BACKGROUND_EMPTY_RIGHT_POS_X,
            const.BACKGROUND_EMPTY_RIGHT_POS_Y,
            const.SQUARE,
            const.CLASSICDENIM,
            const.BACKGROUND_EMPTY_RIGHT_WID,
            const.BACKGROUND_EMPTY_RIGHT_LEN
            )

    def create_background_light(self):
        """Creates light goods platform background."""
        # Light goods platform
        self.background_light = turtle.Turtle()
        self.background_part.update(
            {
                "background_light": self.background_light
            }
        )
        self.initialize_background_part(
            "background_light",
            const.BACKGROUND_LIGHT_HEADING,
            const.BACKGROUND_LIGHT_POS_X,
            const.BACKGROUND_LIGHT_POS_Y,
            const.SQUARE,
            const.BLEACHEDDENIM,
            const.BACKGROUND_LIGHT_WID,
            const.BACKGROUND_LIGHT_LEN
            )

    def create_background_regular(self):
        """Creates regular goods platform background."""
        # Regular goods platform
        self.background_regular = turtle.Turtle()
        self.background_part.update(
            {
                "background_regular": self.background_regular
            }
        )
        self.initialize_background_part(
            "background_regular",
            const.BACKGROUND_REGULAR_HEADING,
            const.BACKGROUND_REGULAR_POS_X,
            const.BACKGROUND_REGULAR_POS_Y,
            const.SQUARE,
            const.OCEANDENIM,
            const.BACKGROUND_REGULAR_WID,
            const.BACKGROUND_REGULAR_LEN
            )

    def create_background_heavy(self):
        """Creates heavy goods platform background."""
        # Heavy goods platform
        self.background_heavy = turtle.Turtle()
        self.background_part.update(
            {
                "background_heavy": self.background_heavy
            }
        )
        self.initialize_background_part(
            "background_heavy",
            const.BACKGROUND_HEAVY_HEADING,
            const.BACKGROUND_HEAVY_POS_X,
            const.BACKGROUND_HEAVY_POS_Y,
            const.SQUARE,
            const.MIDNIGHTDENIM,
            const.BACKGROUND_HEAVY_WID,
            const.BACKGROUND_HEAVY_LEN
            )

    def create_background_conveyor(self):
        """Creates goods conveyor background."""
        # Goods conveyor
        self.background_conveyor = turtle.Turtle()
        self.background_part.update(
            {
                "background_conveyor": self.background_conveyor
            }
        )
        self.initialize_background_part(
            "background_conveyor",
            const.BACKGROUND_CONVEYOR_HEADING,
            const.BACKGROUND_CONVEYOR_POS_X,
            const.BACKGROUND_CONVEYOR_POS_Y,
            const.SQUARE,
            const.CREAM,
            const.BACKGROUND_CONVEYOR_WID,
            const.BACKGROUND_CONVEYOR_LEN
            )

    def positions(self):
        """Set the position for each backround part."""
        self.background_empty_mid_pos_x += 1 * self.direction_term
        self.background_empty_left_pos_x += 1 * self.direction_term
        self.background_empty_right_pos_x += 1 * self.direction_term
        self.background_light_pos_x += 1 * self.direction_term
        self.background_regular_pos_x += 1 * self.direction_term
        self.background_heavy_pos_x += 1 * self.direction_term
        self.background_conveyor_pos_x += 1 * self.direction_term

    def to_start_pos(self):
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

    def to_current_pos(self):
        """Set background parts to current positions."""
        self.background_empty_mid.goto(
            self.background_empty_mid_pos_x,
            const.BACKGROUND_EMPTY_MID_POS_Y
            )
        self.background_empty_left.goto(
            self.background_empty_left_pos_x,
            const.BACKGROUND_EMPTY_LEFT_POS_Y
            )
        self.background_empty_right.goto(
            self.background_empty_right_pos_x,
            const.BACKGROUND_EMPTY_RIGHT_POS_Y
            )
        self.background_light.goto(
            self.background_light_pos_x,
            const.BACKGROUND_LIGHT_POS_Y
            )
        self.background_regular.goto(
            self.background_regular_pos_x,
            const.BACKGROUND_REGULAR_POS_Y
            )
        self.background_heavy.goto(
            self.background_heavy_pos_x,
            const.BACKGROUND_HEAVY_POS_Y
            )
        self.background_conveyor.goto(
            self.background_conveyor_pos_x,
            const.BACKGROUND_CONVEYOR_POS_Y
            )

    def to_extreme_pos(self, term):
        """Set background parts to extreme positions."""
        self.background_empty_mid_pos_x = const.BACKGROUND_EMPTY_MID_POS_X\
            + term
        self.background_empty_left_pos_x = const.BACKGROUND_EMPTY_LEFT_POS_X\
            + term
        self.background_empty_right_pos_x = const.BACKGROUND_EMPTY_RIGHT_POS_X\
            + term
        self.background_light_pos_x = const.BACKGROUND_LIGHT_POS_X\
            + term
        self.background_regular_pos_x = const.BACKGROUND_REGULAR_POS_X\
            + term
        self.background_heavy_pos_x = const.BACKGROUND_HEAVY_POS_X\
            + term
        self.background_conveyor_pos_x = const.BACKGROUND_CONVEYOR_POS_X\
            + term

    def to_leftmost_pos(self):
        """Set background parts to leftmost position."""
        self.to_start_pos()
        self.to_extreme_pos(const.LEFTMOST_TERM)

    def to_rightmost_pos(self):
        """Set background parts to rightmost position."""
        self.to_start_pos()
        self.to_extreme_pos(const.RIGHTMOST_TERM)

    def update_background(self):
        """Update the position of the background."""
        if self.background_empty_left_pos_x == 0 and self.right:
            self.to_leftmost_pos()
        elif self.background_empty_right_pos_x == 0 and self.left:
            self.to_rightmost_pos()
        else:
            self.positions()
            self.to_current_pos()
