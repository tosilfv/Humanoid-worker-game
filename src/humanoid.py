import math
import turtle
import constants as const

class Humanoid:
    """A simple animated humanoid using turtle graphics."""


    def __init__(self):
        """Initialize the humanoid components."""
        self.__body_part = {}
        self.move_speed = {
            "default": 0,
            "slow": 0.01,
            "normal": 0.005,
            "fast": 0.001
            }
        self.humanoid_speed = self.move_speed["default"]
        self.__create_left_leg()
        self.__create_left_arm()
        self.__create_head()
        self.__create_shoulders()
        self.__create_chest()
        self.__create_waist()
        self.__create_pelvis()
        self.__create_right_leg()
        self.__create_right_arm()
        self.__left_thigh_angle = const.THIGH_HEADING
        self.__right_thigh_angle = const.THIGH_HEADING
        self.__left_thigh_extended = False
        self.__left_thigh_retracted = True
        self.__right_thigh_extended = True
        self.__right_thigh_retracted = False
        self.move = False

        # Direction
        self.left = False
        self.right = True

    @property
    def __get_direction_term(self):
        """Return either 1 or -1 depending on humanoid direction."""
        self.__direction_term = (-1 * self.left + self.right)
        return self.__direction_term

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
        self.__body_part[part].speed(0)
        self.__body_part[part].shape(shape)
        self.__body_part[part].color(color)
        self.__body_part[part].shapesize(stretch_wid=wid, stretch_len=len)

    def __create_head(self):
        """Creates the face and cranium."""
        # Face
        self.__face = turtle.Turtle()
        self.__body_part.update(
            {
                "face": self.__face
            }
        )
        self.__initialize_body_part(
            "face",
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
                "cranium": self.__cranium
            }
        )
        self.__initialize_body_part(
            "cranium",
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
                "shoulders": self.__shoulders
            }
        )
        self.__initialize_body_part(
            "shoulders",
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
                "chest": self.__chest
            }
        )
        self.__initialize_body_part(
            "chest",
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
                "waist": self.__waist
            }
        )
        self.__initialize_body_part(
            "waist",
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
                "pelvis": self.__pelvis
            }
        )
        self.__initialize_body_part(
            "pelvis",
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
                "left_thigh": self.__left_thigh
            }
        )
        self.__initialize_body_part(
            "left_thigh",
            const.THIGH_HEADING,
            const.THIGH_POS_X,
            0,
            const.ARROW,
            const.GREY,
            const.THIGH_WID,
            const.THIGH_LEN
            )

        # Left calf
        self.__left_calf = turtle.Turtle()
        self.__body_part.update(
            {
                "left_calf": self.__left_calf
            }
        )
        self.__initialize_body_part(
            "left_calf",
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
                "left_foot": self.__left_foot
            }
        )
        self.__initialize_body_part(
            "left_foot",
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
                "right_thigh": self.__right_thigh
            }
        )
        self.__initialize_body_part(
            "right_thigh",
            const.THIGH_HEADING,
            const.THIGH_POS_X,
            0,
            const.ARROW,
            const.DARKGREY,
            const.THIGH_WID,
            const.THIGH_LEN
            )

        # Right calf
        self.__right_calf = turtle.Turtle()
        self.__body_part.update(
            {
                "right_calf": self.__right_calf
            }
        )
        self.__initialize_body_part(
            "right_calf",
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
                "right_foot": self.__right_foot
            }
        )
        self.__initialize_body_part(
            "right_foot",
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
                "left_upperarm": self.__left_upperarm
            }
        )
        self.__initialize_body_part(
            "left_upperarm",
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
                "left_forearm": self.__left_forearm
            }
        )
        self.__initialize_body_part(
            "left_forearm",
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
                "left_hand": self.__left_hand
            }
        )
        self.__initialize_body_part(
            "left_hand",
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
                "right_upperarm": self.__right_upperarm
            }
        )
        self.__initialize_body_part(
            "right_upperarm",
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
                "right_forearm": self.__right_forearm
            }
        )
        self.__initialize_body_part(
            "right_forearm",
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
                "right_hand": self.__right_hand
            }
        )
        self.__initialize_body_part(
            "right_hand",
            const.HAND_HEADING,
            const.UPPERARM_POS_X,
            (const.UPPERARM_SIZE + const.FOREARM_SIZE) + const.UPPERARM_POS_Y,
            const.SQUARE,
            const.LIGHTGREY,
            const.HAND_WID,
            const.HAND_LEN
            )

    def __angles(self):
        """Set the angle for each thigh to which limb angles are based on."""
        # Left thigh
        if self.__left_thigh_angle == const.MAX_EXTENDED:
            self.__left_thigh_extended = True
            self.__left_thigh_retracted = False
        elif self.__left_thigh_angle == const.MAX_RETRACTED:
            self.__left_thigh_extended = False
            self.__left_thigh_retracted = True
        if self.__left_thigh_extended:
            self.__left_thigh_angle -= 1
        elif self.__left_thigh_retracted:
            self.__left_thigh_angle += 1

        # Right thigh
        if self.__right_thigh_angle == const.MAX_EXTENDED:
            self.__right_thigh_extended = True
            self.__right_thigh_retracted = False
        elif self.__right_thigh_angle == const.MAX_RETRACTED:
            self.__right_thigh_extended = False
            self.__right_thigh_retracted = True
        if self.__right_thigh_extended:
            self.__right_thigh_angle -= 1
        elif self.__right_thigh_retracted:
            self.__right_thigh_angle += 1

    @staticmethod
    def __get_coord_x(angle_x):
        """Get the x coordinate for limbs."""
        return math.cos(math.radians(angle_x))

    @staticmethod
    def __get_coord_y(angle_y):
        """Get the y coordinate for limbs."""
        return math.sin(math.radians(angle_y))

    def update_limbs(self):
        """Updates the angles of all limbs."""
        self.__angles()

        ## Leg angles

        # Left thigh
        self.__left_thigh.setheading(self.__left_thigh_angle)

        # Right thigh
        self.__right_thigh.setheading(self.__right_thigh_angle)

        # Left calf
        self.__left_calf.setheading(self.__left_thigh_angle)
        left_calf_x = const.THIGH_SIZE * self.__get_coord_x(
            self.__left_thigh_angle + const.CALF_POS_X * self.__get_direction_term
            )
        left_calf_y = const.THIGH_SIZE * self.__get_coord_y(
            self.__left_thigh_angle
            )
        self.__left_calf.goto(left_calf_x, left_calf_y + const.THIGH_POS_Y)

        # Right calf
        self.__right_calf.setheading(self.__right_thigh_angle)
        right_calf_x = const.THIGH_SIZE * self.__get_coord_x(
            self.__right_thigh_angle + const.CALF_POS_X * self.__get_direction_term
            )
        right_calf_y = const.THIGH_SIZE * self.__get_coord_y(
            self.__right_thigh_angle
            )
        self.__right_calf.goto(right_calf_x, right_calf_y + const.THIGH_POS_Y)

        # Left foot
        self.__left_foot.setheading(self.__left_thigh_angle)
        left_foot_x = -const.FOOT_POS_Y\
            * self.__get_coord_x(self.__left_thigh_angle)
        left_foot_y = -const.FOOT_POS_Y\
            * self.__get_coord_y(self.__left_thigh_angle)
        self.__left_foot.goto(
            left_foot_x + const.FOOT_POS_X * self.__get_direction_term,
            left_foot_y
            )

        # Right foot
        self.__right_foot.setheading(self.__right_thigh_angle)
        right_foot_x = -const.FOOT_POS_Y\
            * self.__get_coord_x(self.__right_thigh_angle)
        right_foot_y = -const.FOOT_POS_Y\
            * self.__get_coord_y(self.__right_thigh_angle)
        self.__right_foot.goto(
            right_foot_x + const.FOOT_POS_X * self.__get_direction_term,
            right_foot_y
            )


        ## Arm angles

        # Left upper arm
        self.__left_upperarm.setheading(self.__right_thigh_angle)

        # Right upper arm
        self.__right_upperarm.setheading(self.__left_thigh_angle)

        # Left forearm
        self.__left_forearm.setheading(self.__right_thigh_angle)
        left_forearm_x = const.UPPERARM_SIZE\
            * self.__get_coord_x(self.__right_thigh_angle)
        left_forearm_y = const.UPPERARM_SIZE\
            * self.__get_coord_y(self.__right_thigh_angle)
        self.__left_forearm.goto(
            left_forearm_x,
            left_forearm_y + const.UPPERARM_POS_Y
            )

        # Right forearm
        self.__right_forearm.setheading(self.__left_thigh_angle)
        right_forearm_x = const.UPPERARM_SIZE\
            * self.__get_coord_x(self.__left_thigh_angle)
        right_forearm_y = const.UPPERARM_SIZE\
            * self.__get_coord_y(self.__left_thigh_angle)
        self.__right_forearm.goto(
            right_forearm_x,
            right_forearm_y + const.UPPERARM_POS_Y
            )

        # Left hand
        self.__left_hand.setheading(self.__right_thigh_angle)
        left_hand_x = (const.UPPERARM_SIZE + const.FOREARM_SIZE)\
            * self.__get_coord_x(self.__right_thigh_angle)
        left_hand_y = (const.UPPERARM_SIZE + const.FOREARM_SIZE)\
            * self.__get_coord_y(self.__right_thigh_angle)
        self.__left_hand.goto(
            left_hand_x + const.HAND_POS_X * self.__get_direction_term,
            left_hand_y + const.UPPERARM_POS_Y
            )

        # Right hand
        self.__right_hand.setheading(self.__left_thigh_angle)
        right_hand_x = (const.UPPERARM_SIZE + const.FOREARM_SIZE)\
            * self.__get_coord_x(self.__left_thigh_angle)
        right_hand_y = (const.UPPERARM_SIZE + const.FOREARM_SIZE)\
            * self.__get_coord_y(self.__left_thigh_angle)
        self.__right_hand.goto(
            right_hand_x + const.HAND_POS_X * self.__get_direction_term,
            right_hand_y + const.UPPERARM_POS_Y
            )

    def to_start_pos(self):
        """Set limbs to start positions."""
        self.__face.goto(
            const.FACE_POS_X * self.__get_direction_term,
            const.FACE_POS_Y
            )
        self.__cranium.goto(
            const.CRANIUM_POS_X * self.__get_direction_term,
            const.CRANIUM_POS_Y
            )
        self.__shoulders.goto(
            const.SHOULDERS_POS_X * self.__get_direction_term,
            const.SHOULDERS_POS_Y
            )
        self.__chest.goto(
            const.CHEST_POS_X * self.__get_direction_term,
            const.CHEST_POS_Y
            )
        self.__waist.goto(
            const.WAIST_POS_X * self.__get_direction_term,
            const.WAIST_POS_Y
            )
        self.__pelvis.goto(
            const.PELVIS_POS_X * self.__get_direction_term,
            const.PELVIS_POS_Y
            )
        self.__left_thigh.goto(
            const.THIGH_POS_X * self.__get_direction_term,
            const.THIGH_POS_Y
            )
        self.__left_thigh.setheading(const.THIGH_HEADING)
        self.__left_calf.goto(
            const.CALF_POS_X * self.__get_direction_term,
            const.CALF_POS_Y
            )
        self.__left_calf.setheading(const.CALF_HEADING)
        self.__left_foot.goto(
            const.FOOT_POS_X * self.__get_direction_term,
            const.FOOT_POS_Y
            )
        self.__left_foot.setheading(const.FOOT_HEADING)
        self.__right_thigh.goto(
            const.THIGH_POS_X * self.__get_direction_term,
            const.THIGH_POS_Y
            )
        self.__right_thigh.setheading(const.THIGH_HEADING)
        self.__right_calf.goto(
            const.CALF_POS_X * self.__get_direction_term,
            const.CALF_POS_Y
            )
        self.__right_calf.setheading(const.CALF_HEADING)
        self.__right_foot.goto(
            const.FOOT_POS_X * self.__get_direction_term,
            const.FOOT_POS_Y
            )
        self.__right_foot.setheading(const.FOOT_HEADING)
        self.__left_upperarm.goto(
            const.UPPERARM_POS_X * self.__get_direction_term,
            const.UPPERARM_POS_Y
            )
        self.__left_upperarm.setheading(const.UPPERARM_HEADING)
        self.__left_forearm.goto(
            const.FOREARM_POS_X * self.__get_direction_term,
            const.FOREARM_POS_Y
            )
        self.__left_forearm.setheading(const.FOREARM_HEADING)
        self.__left_hand.goto(
            const.HAND_POS_X * self.__get_direction_term,
            const.HAND_POS_Y
            )
        self.__left_hand.setheading(const.HAND_HEADING)
        self.__right_upperarm.goto(
            const.UPPERARM_POS_X * self.__get_direction_term,
            const.UPPERARM_POS_Y
            )
        self.__right_upperarm.setheading(const.UPPERARM_HEADING)
        self.__right_forearm.goto(
            const.FOREARM_POS_X * self.__get_direction_term,
            const.FOREARM_POS_Y
            )
        self.__right_forearm.setheading(const.FOREARM_HEADING)
        self.__right_hand.goto(
            const.HAND_POS_X * self.__get_direction_term,
            const.HAND_POS_Y
            )
        self.__right_hand.setheading(const.HAND_HEADING)

        ## Set angles to start positions.
        self.__left_thigh_angle = const.THIGH_HEADING
        self.__right_thigh_angle = const.THIGH_HEADING
