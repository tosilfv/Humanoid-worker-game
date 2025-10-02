import turtle
import math
from utils import constants as const, direction_term


class Humanoid:
    """An animated humanoid using turtle graphics."""

    def __init__(self):
        """Initialize the humanoid components."""
        self.__body_part = {}
        self._move_speed = {
            "default": const.DEFAULT,
            "slow": const.SLOW,
            "normal": const.NORMAL,
            "fast": const.FAST
            }
        self.__create_left_leg()
        self.__create_left_arm()
        self.__create_head()
        self.__create_shoulders()
        self.__create_chest()
        self.__create_waist()
        self.__create_pelvis()
        self.__create_right_leg()
        self.__create_right_arm()
        self.__left_thigh_heading = const.THIGH_HEADING
        self.__left_thigh_extended = False
        self.__left_thigh_retracted = True
        self.__right_thigh_heading = const.THIGH_HEADING
        self.__right_thigh_extended = True
        self.__right_thigh_retracted = False
        self._humanoid_speed = self._move_speed["default"]
        self._move = False
        self._left = False
        self._right = True
        self._carries_box = False

    @property
    def __direction_heading(self):
        """Get the humanoid direction heading depending on humanoid
        direction.
        """
        if self.left:
            return const.CARRY_LEFT_FOREARM_HEADING
        return const.CARRY_RIGHT_FOREARM_HEADING

    @property
    def body_part(self):
        """Get body part value."""
        return self.__body_part

    @property
    def move_speed(self):
        """Get move speed value."""
        return self._move_speed

    @property
    def left_thigh_heading(self):
        """Get left thigh heading value."""
        return self.__left_thigh_heading

    @property
    def left_thigh_extended(self):
        """Get left thigh extended value."""
        return self.__left_thigh_extended

    @property
    def left_thigh_retracted(self):
        """Get left thigh retracted value."""
        return self.__left_thigh_retracted

    @property
    def right_thigh_heading(self):
        """Get right thigh heading value."""
        return self.__right_thigh_heading

    @property
    def right_thigh_extended(self):
        """Get right thigh extended value."""
        return self.__right_thigh_extended

    @property
    def right_thigh_retracted(self):
        """Get right thigh retracted value."""
        return self.__right_thigh_retracted

    @property
    def humanoid_speed(self):
        """Get humanoid speed."""
        return self._humanoid_speed

    @humanoid_speed.setter
    def humanoid_speed(self, speed):
        """Set humanoid speed value."""
        self._humanoid_speed = speed

    @property
    def move(self):
        """Get move boolean value."""
        return self._move

    @move.setter
    def move(self, is_moving):
        """Set move boolean value."""
        self._move = is_moving

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
    def carries_box(self):
        """Get carries box boolean value."""
        return self._carries_box

    @carries_box.setter
    def carries_box(self, is_carrying):
        """Set carries box boolean value."""
        self._carries_box = is_carrying

    def create_measurement_grid(self):
        """Creates a grid of segments to which measurements are based on."""
        self.__meas_grid = turtle.Turtle()
        self.__meas_grid.hideturtle()
        self.__meas_grid.pencolor(const.RED)
        self.__meas_grid.goto(20, 0)
        self.__meas_grid.goto(20, -25)
        self.__meas_grid.goto(0, -25)
        self.__meas_grid.goto(20, -25)
        self.__meas_grid.goto(20, -50)
        self.__meas_grid.goto(0, -50)
        self.__meas_grid.goto(20, -50)
        self.__meas_grid.goto(20, -75)
        self.__meas_grid.goto(0, -75)
        self.__meas_grid.goto(20, -75)
        self.__meas_grid.goto(20, -100)
        self.__meas_grid.goto(0, -100)
        self.__meas_grid.goto(20, -100)
        self.__meas_grid.goto(20, 0)
        self.__meas_grid.goto(20, 25)
        self.__meas_grid.goto(0, 25)
        self.__meas_grid.goto(20, 25)
        self.__meas_grid.goto(20, 50)
        self.__meas_grid.goto(0, 50)
        self.__meas_grid.goto(20, 50)
        self.__meas_grid.goto(20, 75)
        self.__meas_grid.goto(0, 75)
        self.__meas_grid.goto(20, 75)
        self.__meas_grid.goto(20, 100)
        self.__meas_grid.goto(0, 100)
        self.__meas_grid.goto(20, 100)
        self.__meas_grid.speed(0)
        self.__meas_grid.shape("classic")
        self.__meas_grid.color(const.RED)

    def __initialize_body_part(
            self, part, heading, goto_x, goto_y, shape, color, wid, len
            ):
        """Set the body part start properties."""
        self.__body_part[part].penup()
        self.__body_part[part].setheading(heading)
        self.__body_part[part].goto(goto_x, goto_y)
        self.__body_part[part].speed(const.SPEED)
        self.__body_part[part].shape(shape)
        self.__body_part[part].color(color)
        self.__body_part[part].shapesize(
            stretch_wid=wid,
            stretch_len=len
            )

    def __create_head(self):
        """Creates the face and the cranium."""
        # Face
        self.__face = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_FACE: self.__face
            }
        )
        self.__initialize_body_part(
            const.NAME_FACE,
            const.FACE_HEADING,
            const.FACE_POS_X,
            const.FACE_POS_Y,
            const.CIRCLE,
            const.DARKGREY,
            const.FACE_WID,
            const.FACE_LEN
            )

        # Cranium
        self.__cranium = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_CRANIUM: self.__cranium
            }
        )
        self.__initialize_body_part(
            const.NAME_CRANIUM,
            const.CRANIUM_HEADING,
            const.CRANIUM_POS_X,
            const.CRANIUM_POS_Y,
            const.CIRCLE,
            const.DARKGREY,
            const.CRANIUM_WID,
            const.CRANIUM_LEN
            )

    def __create_shoulders(self):
        """Creates the shoulders."""
        # Shoulders
        self.__shoulders = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_SHOULDERS: self.__shoulders
            }
        )
        self.__initialize_body_part(
            const.NAME_SHOULDERS,
            const.SHOULDERS_HEADING,
            const.SHOULDERS_POS_X,
            const.SHOULDERS_POS_Y,
            const.TRIANGLE,
            const.DARKGREY,
            const.SHOULDERS_WID,
            const.SHOULDERS_LEN
            )

    def __create_chest(self):
        """Creates the chest."""
        # Chest
        self.__chest = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_CHEST: self.__chest
            }
        )
        self.__initialize_body_part(
            const.NAME_CHEST,
            const.CHEST_HEADING,
            const.CHEST_POS_X,
            const.CHEST_POS_Y,
            const.SQUARE,
            const.DARKGREY,
            const.CHEST_WID,
            const.CHEST_LEN
            )

    def __create_waist(self):
        """Creates the waist."""
        # Waist
        self.__waist = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_WAIST: self.__waist
            }
        )
        self.__initialize_body_part(
            const.NAME_WAIST,
            const.WAIST_HEADING,
            const.WAIST_POS_X,
            const.WAIST_POS_Y,
            const.TRIANGLE,
            const.DARKGREY,
            const.WAIST_WID,
            const.WAIST_LEN
            )

    def __create_pelvis(self):
        """Creates the pelvis."""
        # Pelvis
        self.__pelvis = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_PELVIS: self.__pelvis
            }
        )
        self.__initialize_body_part(
            const.NAME_PELVIS,
            const.PELVIS_HEADING,
            const.PELVIS_POS_X,
            const.PELVIS_POS_Y,
            const.SQUARE,
            const.DARKGREY,
            const.PELVIS_WID,
            const.PELVIS_LEN
            )

    def __create_left_leg(self):
        """Creates the left thigh, calf and foot."""
        # Left thigh
        self.__left_thigh = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_LEFT_THIGH: self.__left_thigh
            }
        )
        self.__initialize_body_part(
            const.NAME_LEFT_THIGH,
            const.THIGH_HEADING,
            const.THIGH_POS_X,
            const.THIGH_POS_Y,
            const.ARROW,
            const.GREY,
            const.THIGH_WID,
            const.THIGH_LEN
            )

        # Left calf
        self.__left_calf = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_LEFT_CALF: self.__left_calf
            }
        )
        self.__initialize_body_part(
            const.NAME_LEFT_CALF,
            const.CALF_HEADING,
            const.THIGH_POS_X,
            -const.THIGH_SIZE,
            const.ARROW,
            const.GREY,
            const.CALF_WID,
            const.CALF_LEN
            )

        # Left foot
        self.__left_foot = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_LEFT_FOOT: self.__left_foot
            }
        )
        self.__initialize_body_part(
            const.NAME_LEFT_FOOT,
            const.FOOT_HEADING,
            const.THIGH_POS_X,
            -(const.THIGH_SIZE + const.CALF_SIZE) + const.THIGH_POS_Y,
            const.SQUARE,
            const.GREY,
            const.FOOT_WID,
            const.FOOT_LEN
            )

    def __create_right_leg(self):
        """Creates the right thigh, calf and foot."""
        # Right thigh
        self.__right_thigh = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_RIGHT_THIGH: self.__right_thigh
            }
        )
        self.__initialize_body_part(
            const.NAME_RIGHT_THIGH,
            const.THIGH_HEADING,
            const.THIGH_POS_X,
            const.THIGH_POS_Y,
            const.ARROW,
            const.DARKGREY,
            const.THIGH_WID,
            const.THIGH_LEN
            )

        # Right calf
        self.__right_calf = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_RIGHT_CALF: self.__right_calf
            }
        )
        self.__initialize_body_part(
            const.NAME_RIGHT_CALF,
            const.CALF_HEADING,
            const.THIGH_POS_X,
            -const.THIGH_SIZE,
            const.ARROW,
            const.DARKGREY,
            const.CALF_WID,
            const.CALF_LEN
            )

        # Right foot
        self.__right_foot = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_RIGHT_FOOT: self.__right_foot
            }
        )
        self.__initialize_body_part(
            const.NAME_RIGHT_FOOT,
            const.FOOT_HEADING,
            const.THIGH_POS_X,
            -(const.THIGH_SIZE + const.CALF_SIZE) + const.THIGH_POS_Y,
            const.SQUARE,
            const.DARKGREY,
            const.FOOT_WID,
            const.FOOT_LEN
            )

    def __create_left_arm(self):
        """Creates the left upper arm, forearm and hand."""
        # Left upper arm
        self.__left_upperarm = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_LEFT_UPPERARM: self.__left_upperarm
            }
        )
        self.__initialize_body_part(
            const.NAME_LEFT_UPPERARM,
            const.UPPERARM_HEADING,
            const.UPPERARM_POS_X,
            const.UPPERARM_POS_Y,
            const.ARROW,
            const.GREY,
            const.UPPERARM_WID,
            const.UPPERARM_LEN
            )

        # Left forearm
        self.__left_forearm = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_LEFT_FOREARM: self.__left_forearm
            }
        )
        self.__initialize_body_part(
            const.NAME_LEFT_FOREARM,
            const.FOREARM_HEADING,
            const.UPPERARM_POS_X,
            const.UPPERARM_SIZE + const.UPPERARM_POS_Y,
            const.ARROW,
            const.GREY,
            const.FOREARM_WID,
            const.FOREARM_LEN
            )

        # Left hand
        self.__left_hand = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_LEFT_HAND: self.__left_hand
            }
        )
        self.__initialize_body_part(
            const.NAME_LEFT_HAND,
            const.HAND_HEADING,
            const.UPPERARM_POS_X,
            (const.UPPERARM_SIZE + const.FOREARM_SIZE) + const.UPPERARM_POS_Y,
            const.SQUARE,
            const.GREY,
            const.HAND_WID,
            const.HAND_LEN
            )

    def __create_right_arm(self):
        """Creates the right upper arm, forearm and hand."""
        # Right upper arm
        self.__right_upperarm = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_RIGHT_UPPERARM: self.__right_upperarm
            }
        )
        self.__initialize_body_part(
            const.NAME_RIGHT_UPPERARM,
            const.UPPERARM_HEADING,
            const.UPPERARM_POS_X,
            const.UPPERARM_POS_Y,
            const.ARROW,
            const.LIGHTGREY,
            const.UPPERARM_WID,
            const.UPPERARM_LEN
            )

        # Right forearm
        self.__right_forearm = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_RIGHT_FOREARM: self.__right_forearm
            }
        )
        self.__initialize_body_part(
            const.NAME_RIGHT_FOREARM,
            const.FOREARM_HEADING,
            const.UPPERARM_POS_X,
            const.UPPERARM_SIZE + const.UPPERARM_POS_Y,
            const.ARROW,
            const.LIGHTGREY,
            const.FOREARM_WID,
            const.FOREARM_LEN
            )

        # Right hand
        self.__right_hand = turtle.Turtle()
        self.__body_part.update(
            {
                const.NAME_RIGHT_HAND: self.__right_hand
            }
        )
        self.__initialize_body_part(
            const.NAME_RIGHT_HAND,
            const.HAND_HEADING,
            const.UPPERARM_POS_X,
            (const.UPPERARM_SIZE + const.FOREARM_SIZE) + const.UPPERARM_POS_Y,
            const.SQUARE,
            const.LIGHTGREY,
            const.HAND_WID,
            const.HAND_LEN
            )

    def __headings(self):
        """Set the headings for each thigh to which limb headings are based
        on.
        """
        # Left thigh
        if self.__left_thigh_heading == const.MAX_EXTENDED:
            self.__left_thigh_extended = True
            self.__left_thigh_retracted = False
        elif self.__left_thigh_heading == const.MAX_RETRACTED:
            self.__left_thigh_extended = False
            self.__left_thigh_retracted = True
        if self.__left_thigh_extended:
            self.__left_thigh_heading -= 1
        elif self.__left_thigh_retracted:
            self.__left_thigh_heading += 1

        # Right thigh
        if self.__right_thigh_heading == const.MAX_EXTENDED:
            self.__right_thigh_extended = True
            self.__right_thigh_retracted = False
        elif self.__right_thigh_heading == const.MAX_RETRACTED:
            self.__right_thigh_extended = False
            self.__right_thigh_retracted = True
        if self.__right_thigh_extended:
            self.__right_thigh_heading -= 1
        elif self.__right_thigh_retracted:
            self.__right_thigh_heading += 1

    @staticmethod
    def __get_coord_x(heading_x):
        """Get the x coordinate for limbs."""
        return math.cos(math.radians(heading_x))

    @staticmethod
    def __get_coord_y(heading_y):
        """Get the y coordinate for limbs."""
        return math.sin(math.radians(heading_y))

    def hands_to_carry(self):
        """Changes hands to carry position."""
        # Left upper arm
        self.__left_upperarm.setheading(const.CARRY_UPPERARM_HEADING)
        self.__left_upperarm.goto(
            const.UPPERARM_POS_X * direction_term(self.left, self.right),
            const.UPPERARM_POS_Y
        )

        # Left forearm
        self.__left_forearm.setheading(self.__direction_heading)
        self.__left_forearm.goto(
            const.CARRY_LEFT_FOREARM_POS_X,
            const.CARRY_LEFT_FOREARM_POS_Y + const.UPPERARM_POS_Y
            )

        # Left hand
        self.__left_hand.setheading(const.HAND_HEADING)
        self.__left_hand.goto(
            const.CARRY_LEFT_HAND_POS_X * direction_term(
                self.left,
                self.right
                ),
            const.CARRY_LEFT_HAND_POS_Y + const.UPPERARM_POS_Y
            )

        # Right upper arm
        self.__right_upperarm.setheading(const.CARRY_UPPERARM_HEADING)
        self.__right_upperarm.goto(
            const.UPPERARM_POS_X * direction_term(self.left, self.right),
            const.UPPERARM_POS_Y
        )

        # Right forearm
        self.__right_forearm.setheading(self.__direction_heading)
        self.__right_forearm.goto(
            const.CARRY_RIGHT_FOREARM_POS_X,
            const.CARRY_RIGHT_FOREARM_POS_Y + const.UPPERARM_POS_Y
            )

        # Right hand
        self.__right_hand.setheading(const.HAND_HEADING)
        self.__right_hand.goto(
            const.CARRY_RIGHT_HAND_POS_X * direction_term(
                self.left,
                self.right
                ),
            const.CARRY_RIGHT_HAND_POS_Y + const.UPPERARM_POS_Y
            )

    def update_limbs(self):
        """Updates the headings of all limbs."""
        self.__headings()

        ## Leg headings

        # Left thigh
        self.__left_thigh.setheading(self.__left_thigh_heading)

        # Left calf
        self.__left_calf.setheading(self.__left_thigh_heading)
        left_calf_x = const.THIGH_SIZE * self.__get_coord_x(
            self.__left_thigh_heading
            + const.CALF_POS_X * direction_term(
                self.left, self.right
                )
            )
        left_calf_y = const.THIGH_SIZE * self.__get_coord_y(
            self.__left_thigh_heading
            )
        self.__left_calf.goto(left_calf_x, left_calf_y + const.THIGH_POS_Y)

        # Left foot
        self.__left_foot.setheading(self.__left_thigh_heading)
        left_foot_x = -const.FOOT_POS_Y\
            * self.__get_coord_x(self.__left_thigh_heading)
        left_foot_y = -const.FOOT_POS_Y\
            * self.__get_coord_y(self.__left_thigh_heading)
        self.__left_foot.goto(
            left_foot_x + const.FOOT_POS_X * direction_term(
                self.left, self.right
                ),
            left_foot_y
            )

        # Right thigh
        self.__right_thigh.setheading(self.__right_thigh_heading)

        # Right calf
        self.__right_calf.setheading(self.__right_thigh_heading)
        right_calf_x = const.THIGH_SIZE * self.__get_coord_x(
            self.__right_thigh_heading
            + const.CALF_POS_X * direction_term(self.left, self.right)
            )
        right_calf_y = const.THIGH_SIZE * self.__get_coord_y(
            self.__right_thigh_heading
            )
        self.__right_calf.goto(right_calf_x, right_calf_y + const.THIGH_POS_Y)

        # Right foot
        self.__right_foot.setheading(self.__right_thigh_heading)
        right_foot_x = -const.FOOT_POS_Y\
            * self.__get_coord_x(self.__right_thigh_heading)
        right_foot_y = -const.FOOT_POS_Y\
            * self.__get_coord_y(self.__right_thigh_heading)
        self.__right_foot.goto(
            right_foot_x + const.FOOT_POS_X * direction_term(
                self.left, self.right
                ),
            right_foot_y
            )


        ## Arm headings

        if self._carries_box:
            self.hands_to_carry()
        else:
            # Left upper arm
            self.__left_upperarm.setheading(self.__right_thigh_heading)

            # Left forearm
            self.__left_forearm.setheading(self.__right_thigh_heading)
            left_forearm_x = const.UPPERARM_SIZE\
                * self.__get_coord_x(self.__right_thigh_heading)
            left_forearm_y = const.UPPERARM_SIZE\
                * self.__get_coord_y(self.__right_thigh_heading)
            self.__left_forearm.goto(
                left_forearm_x,
                left_forearm_y + const.UPPERARM_POS_Y
                )

            # Left hand
            self.__left_hand.setheading(self.__right_thigh_heading)
            left_hand_x = (const.UPPERARM_SIZE + const.FOREARM_SIZE)\
                * self.__get_coord_x(self.__right_thigh_heading)
            left_hand_y = (const.UPPERARM_SIZE + const.FOREARM_SIZE)\
                * self.__get_coord_y(self.__right_thigh_heading)
            self.__left_hand.goto(
                left_hand_x + const.HAND_POS_X * direction_term(
                    self.left, self.right
                    ),
                left_hand_y + const.UPPERARM_POS_Y
                )

            # Right upper arm
            self.__right_upperarm.setheading(self.__left_thigh_heading)

            # Right forearm
            self.__right_forearm.setheading(self.__left_thigh_heading)
            right_forearm_x = const.UPPERARM_SIZE\
                * self.__get_coord_x(self.__left_thigh_heading)
            right_forearm_y = const.UPPERARM_SIZE\
                * self.__get_coord_y(self.__left_thigh_heading)
            self.__right_forearm.goto(
                right_forearm_x,
                right_forearm_y + const.UPPERARM_POS_Y
                )

            # Right hand
            self.__right_hand.setheading(self.__left_thigh_heading)
            right_hand_x = (const.UPPERARM_SIZE + const.FOREARM_SIZE)\
                * self.__get_coord_x(self.__left_thigh_heading)
            right_hand_y = (const.UPPERARM_SIZE + const.FOREARM_SIZE)\
                * self.__get_coord_y(self.__left_thigh_heading)
            self.__right_hand.goto(
                right_hand_x + const.HAND_POS_X * direction_term(
                    self.left, self.right
                    ),
                right_hand_y + const.UPPERARM_POS_Y
                )

    def to_start_pos(self):
        """Set limbs to start positions."""
        self.__face.goto(
            const.FACE_POS_X * direction_term(self.left, self.right),
            const.FACE_POS_Y
            )
        self.__cranium.goto(
            const.CRANIUM_POS_X * direction_term(self.left, self.right),
            const.CRANIUM_POS_Y
            )
        self.__shoulders.goto(
            const.SHOULDERS_POS_X * direction_term(self.left, self.right),
            const.SHOULDERS_POS_Y
            )
        self.__chest.goto(
            const.CHEST_POS_X * direction_term(self.left, self.right),
            const.CHEST_POS_Y
            )
        self.__waist.goto(
            const.WAIST_POS_X * direction_term(self.left, self.right),
            const.WAIST_POS_Y
            )
        self.__pelvis.goto(
            const.PELVIS_POS_X * direction_term(self.left, self.right),
            const.PELVIS_POS_Y
            )
        self.__left_thigh.goto(
            const.THIGH_POS_X * direction_term(self.left, self.right),
            const.THIGH_POS_Y
            )
        self.__left_thigh.setheading(const.THIGH_HEADING)
        self.__left_calf.goto(
            const.CALF_POS_X * direction_term(self.left, self.right),
            const.CALF_POS_Y
            )
        self.__left_calf.setheading(const.CALF_HEADING)
        self.__left_foot.goto(
            const.FOOT_POS_X * direction_term(self.left, self.right),
            const.FOOT_POS_Y
            )
        self.__left_foot.setheading(const.FOOT_HEADING)
        self.__right_thigh.goto(
            const.THIGH_POS_X * direction_term(self.left, self.right),
            const.THIGH_POS_Y
            )
        self.__right_thigh.setheading(const.THIGH_HEADING)
        self.__right_calf.goto(
            const.CALF_POS_X * direction_term(self.left, self.right),
            const.CALF_POS_Y
            )
        self.__right_calf.setheading(const.CALF_HEADING)
        self.__right_foot.goto(
            const.FOOT_POS_X * direction_term(self.left, self.right),
            const.FOOT_POS_Y
            )
        self.__right_foot.setheading(const.FOOT_HEADING)
        self.__left_upperarm.goto(
            const.UPPERARM_POS_X * direction_term(self.left, self.right),
            const.UPPERARM_POS_Y
            )

        # Carries box
        if self._carries_box:
            self.hands_to_carry()
        else:
            self.__left_upperarm.setheading(const.UPPERARM_HEADING)
            self.__left_forearm.goto(
                const.FOREARM_POS_X * direction_term(self.left, self.right),
                const.FOREARM_POS_Y
                )
            self.__left_forearm.setheading(const.FOREARM_HEADING)
            self.__left_hand.goto(
                const.HAND_POS_X * direction_term(self.left, self.right),
                const.HAND_POS_Y
                )
            self.__left_hand.setheading(const.HAND_HEADING)
            self.__right_upperarm.goto(
                const.UPPERARM_POS_X * direction_term(self.left, self.right),
                const.UPPERARM_POS_Y
                )
            self.__right_upperarm.setheading(const.UPPERARM_HEADING)
            self.__right_forearm.goto(
                const.FOREARM_POS_X * direction_term(self.left, self.right),
                const.FOREARM_POS_Y
                )
            self.__right_forearm.setheading(const.FOREARM_HEADING)
            self.__right_hand.goto(
                const.HAND_POS_X * direction_term(self.left, self.right),
                const.HAND_POS_Y
                )
            self.__right_hand.setheading(const.HAND_HEADING)

        ## Set headings to start positions.
        self.__left_thigh_heading = const.THIGH_HEADING
        self.__right_thigh_heading = const.THIGH_HEADING
