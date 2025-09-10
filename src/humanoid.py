import math
import turtle
import constants as const

class Humanoid:
    """A simple animated humanoid using turtle graphics."""


    def __init__(self):
        """Initialize the humanoid components."""
        self.body_part = {}
        self.move_speed = {
            "default": 0,
            "slow": 0.01,
            "normal": 0.005,
            "fast": 0.001
            }
        self.humanoid_speed = self.move_speed["default"]
        self.create_left_leg()
        self.create_left_arm()
        self.create_head()
        self.create_shoulders()
        self.create_chest()
        self.create_waist()
        self.create_pelvis()
        self.create_right_leg()
        self.create_right_arm()

        ## Uncomment to show grid.
        # self.create_measurement_grid()
        self.left_thigh_angle = const.THIGH_HEADING
        self.right_thigh_angle = const.THIGH_HEADING
        self.left_thigh_extended = False
        self.left_thigh_retracted = True
        self.right_thigh_extended = True
        self.right_thigh_retracted = False
        self.move = False

        # Direction
        self.left = False
        self.right = True

    @property
    def direction_term(self):
        """Return either 1 or -1 depending on humanoid direction."""
        self._direction_term = (-1 * self.left + self.right)
        return self._direction_term

    def create_measurement_grid(self):
        """Creates a grid of segments to which measurements are based on."""
        self.meas_grid = turtle.Turtle()
        self.meas_grid.hideturtle()
        self.meas_grid.pencolor(const.RED)
        self.meas_grid.goto(20, 0)
        self.meas_grid.goto(20, -25)
        self.meas_grid.goto(0, -25)
        self.meas_grid.goto(20, -25)
        self.meas_grid.goto(20, -50)
        self.meas_grid.goto(0, -50)
        self.meas_grid.goto(20, -50)
        self.meas_grid.goto(20, -75)
        self.meas_grid.goto(0, -75)
        self.meas_grid.goto(20, -75)
        self.meas_grid.goto(20, -100)
        self.meas_grid.goto(0, -100)
        self.meas_grid.goto(20, -100)
        self.meas_grid.goto(20, 0)
        self.meas_grid.goto(20, 25)
        self.meas_grid.goto(0, 25)
        self.meas_grid.goto(20, 25)
        self.meas_grid.goto(20, 50)
        self.meas_grid.goto(0, 50)
        self.meas_grid.goto(20, 50)
        self.meas_grid.goto(20, 75)
        self.meas_grid.goto(0, 75)
        self.meas_grid.goto(20, 75)
        self.meas_grid.goto(20, 100)
        self.meas_grid.goto(0, 100)
        self.meas_grid.goto(20, 100)
        self.meas_grid.speed(0)
        self.meas_grid.shape("classic")
        self.meas_grid.color(const.RED)

    def initialize_body_part(
            self, part, heading, goto_x, goto_y, shape, color, wid, len
            ):
        """Set the body part start properties."""
        self.body_part[part].penup()
        self.body_part[part].setheading(heading)
        self.body_part[part].goto(goto_x, goto_y)
        self.body_part[part].speed(0)
        self.body_part[part].shape(shape)
        self.body_part[part].color(color)
        self.body_part[part].shapesize(stretch_wid=wid, stretch_len=len)

    def create_head(self):
        """Creates the face and cranium."""
        # Face
        self.face = turtle.Turtle()
        self.body_part.update(
            {
                "face": self.face
            }
        )
        self.initialize_body_part(
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
        self.cranium = turtle.Turtle()
        self.body_part.update(
            {
                "cranium": self.cranium
            }
        )
        self.initialize_body_part(
            "cranium",
            const.CRANIUM_HEADING,
            const.CRANIUM_POS_X,
            const.CRANIUM_POS_Y,
            const.CIRCLE,
            const.DARKGREY,
            const.CRANIUM_WID,
            const.CRANIUM_LEN
            )

    def create_shoulders(self):
        """Creates the shoulders."""
        # Shoulders
        self.shoulders = turtle.Turtle()
        self.body_part.update(
            {
                "shoulders": self.shoulders
            }
        )
        self.initialize_body_part(
            "shoulders",
            const.SHOULDERS_HEADING,
            const.SHOULDERS_POS_X,
            const.SHOULDERS_POS_Y,
            const.TRIANGLE,
            const.DARKGREY,
            const.SHOULDERS_WID,
            const.SHOULDERS_LEN
            )

    def create_chest(self):
        """Creates the chest."""
        # Chest
        self.chest = turtle.Turtle()
        self.body_part.update(
            {
                "chest": self.chest
            }
        )
        self.initialize_body_part(
            "chest",
            const.CHEST_HEADING,
            const.CHEST_POS_X,
            const.CHEST_POS_Y,
            const.SQUARE,
            const.DARKGREY,
            const.CHEST_WID,
            const.CHEST_LEN
            )

    def create_waist(self):
        """Creates the waist."""
        # Waist
        self.waist = turtle.Turtle()
        self.body_part.update(
            {
                "waist": self.waist
            }
        )
        self.initialize_body_part(
            "waist",
            const.WAIST_HEADING,
            const.WAIST_POS_X,
            const.WAIST_POS_Y,
            const.TRIANGLE,
            const.DARKGREY,
            const.WAIST_WID,
            const.WAIST_LEN
            )

    def create_pelvis(self):
        """Creates the pelvis."""
        # Pelvis
        self.pelvis = turtle.Turtle()
        self.body_part.update(
            {
                "pelvis": self.pelvis
            }
        )
        self.initialize_body_part(
            "pelvis",
            const.PELVIS_HEADING,
            const.PELVIS_POS_X,
            const.PELVIS_POS_Y,
            const.SQUARE,
            const.DARKGREY,
            const.PELVIS_WID,
            const.PELVIS_LEN
            )

    def create_left_leg(self):
        """Creates the left thigh, calf and foot."""
        # Left thigh
        self.left_thigh = turtle.Turtle()
        self.body_part.update(
            {
                "left_thigh": self.left_thigh
            }
        )
        self.initialize_body_part(
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
        self.left_calf = turtle.Turtle()
        self.body_part.update(
            {
                "left_calf": self.left_calf
            }
        )
        self.initialize_body_part(
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
        self.left_foot = turtle.Turtle()
        self.body_part.update(
            {
                "left_foot": self.left_foot
            }
        )
        self.initialize_body_part(
            "left_foot",
            const.FOOT_HEADING,
            const.THIGH_POS_X,
            -(const.THIGH_SIZE + const.CALF_SIZE) + const.THIGH_POS_Y,
            const.SQUARE,
            const.GREY,
            const.FOOT_WID,
            const.FOOT_LEN
            )

    def create_right_leg(self):
        """Creates the right thigh, calf and foot."""
        # Right thigh
        self.right_thigh = turtle.Turtle()
        self.body_part.update(
            {
                "right_thigh": self.right_thigh
            }
        )
        self.initialize_body_part(
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
        self.right_calf = turtle.Turtle()
        self.body_part.update(
            {
                "right_calf": self.right_calf
            }
        )
        self.initialize_body_part(
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
        self.right_foot = turtle.Turtle()
        self.body_part.update(
            {
                "right_foot": self.right_foot
            }
        )
        self.initialize_body_part(
            "right_foot",
            const.FOOT_HEADING,
            const.THIGH_POS_X,
            -(const.THIGH_SIZE + const.CALF_SIZE) + const.THIGH_POS_Y,
            const.SQUARE,
            const.DARKGREY,
            const.FOOT_WID,
            const.FOOT_LEN
            )

    def create_left_arm(self):
        """Creates the left upper arm, forearm and hand."""
        # Left upper arm
        self.left_upperarm = turtle.Turtle()
        self.body_part.update(
            {
                "left_upperarm": self.left_upperarm
            }
        )
        self.initialize_body_part(
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
        self.left_forearm = turtle.Turtle()
        self.body_part.update(
            {
                "left_forearm": self.left_forearm
            }
        )
        self.initialize_body_part(
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
        self.left_hand = turtle.Turtle()
        self.body_part.update(
            {
                "left_hand": self.left_hand
            }
        )
        self.initialize_body_part(
            "left_hand",
            const.HAND_HEADING,
            const.UPPERARM_POS_X,
            (const.UPPERARM_SIZE + const.FOREARM_SIZE) + const.UPPERARM_POS_Y,
            const.SQUARE,
            const.GREY,
            const.HAND_WID,
            const.HAND_LEN
            )

    def create_right_arm(self):
        """Creates the right upper arm, forearm and hand."""
        # Right upper arm
        self.right_upperarm = turtle.Turtle()
        self.body_part.update(
            {
                "right_upperarm": self.right_upperarm
            }
        )
        self.initialize_body_part(
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
        self.right_forearm = turtle.Turtle()
        self.body_part.update(
            {
                "right_forearm": self.right_forearm
            }
        )
        self.initialize_body_part(
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
        self.right_hand = turtle.Turtle()
        self.body_part.update(
            {
                "right_hand": self.right_hand
            }
        )
        self.initialize_body_part(
            "right_hand",
            const.HAND_HEADING,
            const.UPPERARM_POS_X,
            (const.UPPERARM_SIZE + const.FOREARM_SIZE) + const.UPPERARM_POS_Y,
            const.SQUARE,
            const.LIGHTGREY,
            const.HAND_WID,
            const.HAND_LEN
            )

    def angles(self):
        """Set the angle for each thigh to which limb angles are based on."""
        # Left thigh
        if self.left_thigh_angle == const.MAX_EXTENDED:
            self.left_thigh_extended = True
            self.left_thigh_retracted = False
        elif self.left_thigh_angle == const.MAX_RETRACTED:
            self.left_thigh_extended = False
            self.left_thigh_retracted = True
        if self.left_thigh_extended:
            self.left_thigh_angle -= 1
        elif self.left_thigh_retracted:
            self.left_thigh_angle += 1

        # Right thigh
        if self.right_thigh_angle == const.MAX_EXTENDED:
            self.right_thigh_extended = True
            self.right_thigh_retracted = False
        elif self.right_thigh_angle == const.MAX_RETRACTED:
            self.right_thigh_extended = False
            self.right_thigh_retracted = True
        if self.right_thigh_extended:
            self.right_thigh_angle -= 1
        elif self.right_thigh_retracted:
            self.right_thigh_angle += 1

    @staticmethod
    def get_coord_x(angle_x):
        """Get the x coordinate for limbs."""
        return math.cos(math.radians(angle_x))

    @staticmethod
    def get_coord_y(angle_y):
        """Get the y coordinate for limbs."""
        return math.sin(math.radians(angle_y))

    def update_limbs(self):
        """Updates the angles of all limbs."""
        self.angles()

        ## Leg angles

        # Left thigh
        self.left_thigh.setheading(self.left_thigh_angle)

        # Right thigh
        self.right_thigh.setheading(self.right_thigh_angle)

        # Left calf
        self.left_calf.setheading(self.left_thigh_angle)
        left_calf_x = const.THIGH_SIZE * self.get_coord_x(
            self.left_thigh_angle + const.CALF_POS_X * self.direction_term
            )
        left_calf_y = const.THIGH_SIZE * self.get_coord_y(
            self.left_thigh_angle
            )
        self.left_calf.goto(left_calf_x, left_calf_y + const.THIGH_POS_Y)

        # Right calf
        self.right_calf.setheading(self.right_thigh_angle)
        right_calf_x = const.THIGH_SIZE * self.get_coord_x(
            self.right_thigh_angle + const.CALF_POS_X * self.direction_term
            )
        right_calf_y = const.THIGH_SIZE * self.get_coord_y(
            self.right_thigh_angle
            )
        self.right_calf.goto(right_calf_x, right_calf_y + const.THIGH_POS_Y)

        # Left foot
        self.left_foot.setheading(self.left_thigh_angle)
        left_foot_x = -const.FOOT_POS_Y\
            * self.get_coord_x(self.left_thigh_angle)
        left_foot_y = -const.FOOT_POS_Y\
            * self.get_coord_y(self.left_thigh_angle)
        self.left_foot.goto(
            left_foot_x + const.FOOT_POS_X * self.direction_term,
            left_foot_y
            )

        # Right foot
        self.right_foot.setheading(self.right_thigh_angle)
        right_foot_x = -const.FOOT_POS_Y\
            * self.get_coord_x(self.right_thigh_angle)
        right_foot_y = -const.FOOT_POS_Y\
            * self.get_coord_y(self.right_thigh_angle)
        self.right_foot.goto(
            right_foot_x + const.FOOT_POS_X * self.direction_term,
            right_foot_y
            )


        ## Arm angles

        # Left upper arm
        self.left_upperarm.setheading(self.right_thigh_angle)

        # Right upper arm
        self.right_upperarm.setheading(self.left_thigh_angle)

        # Left forearm
        self.left_forearm.setheading(self.right_thigh_angle)
        left_forearm_x = const.UPPERARM_SIZE\
            * self.get_coord_x(self.right_thigh_angle)
        left_forearm_y = const.UPPERARM_SIZE\
            * self.get_coord_y(self.right_thigh_angle)
        self.left_forearm.goto(
            left_forearm_x,
            left_forearm_y + const.UPPERARM_POS_Y
            )

        # Right forearm
        self.right_forearm.setheading(self.left_thigh_angle)
        right_forearm_x = const.UPPERARM_SIZE\
            * self.get_coord_x(self.left_thigh_angle)
        right_forearm_y = const.UPPERARM_SIZE\
            * self.get_coord_y(self.left_thigh_angle)
        self.right_forearm.goto(
            right_forearm_x,
            right_forearm_y + const.UPPERARM_POS_Y
            )

        # Left hand
        self.left_hand.setheading(self.right_thigh_angle)
        left_hand_x = (const.UPPERARM_SIZE + const.FOREARM_SIZE)\
            * self.get_coord_x(self.right_thigh_angle)
        left_hand_y = (const.UPPERARM_SIZE + const.FOREARM_SIZE)\
            * self.get_coord_y(self.right_thigh_angle)
        self.left_hand.goto(
            left_hand_x + const.HAND_POS_X * self.direction_term,
            left_hand_y + const.UPPERARM_POS_Y
            )

        # Right hand
        self.right_hand.setheading(self.left_thigh_angle)
        right_hand_x = (const.UPPERARM_SIZE + const.FOREARM_SIZE)\
            * self.get_coord_x(self.left_thigh_angle)
        right_hand_y = (const.UPPERARM_SIZE + const.FOREARM_SIZE)\
            * self.get_coord_y(self.left_thigh_angle)
        self.right_hand.goto(
            right_hand_x + const.HAND_POS_X * self.direction_term,
            right_hand_y + const.UPPERARM_POS_Y
            )

    def to_start_pos(self):
        """Set limbs to start positions."""
        self.face.goto(
            const.FACE_POS_X * self.direction_term,
            const.FACE_POS_Y
            )
        self.cranium.goto(
            const.CRANIUM_POS_X * self.direction_term,
            const.CRANIUM_POS_Y
            )
        self.shoulders.goto(
            const.SHOULDERS_POS_X * self.direction_term,
            const.SHOULDERS_POS_Y
            )
        self.chest.goto(
            const.CHEST_POS_X * self.direction_term,
            const.CHEST_POS_Y
            )
        self.waist.goto(
            const.WAIST_POS_X * self.direction_term,
            const.WAIST_POS_Y
            )
        self.pelvis.goto(
            const.PELVIS_POS_X * self.direction_term,
            const.PELVIS_POS_Y
            )
        self.left_thigh.goto(
            const.THIGH_POS_X * self.direction_term,
            const.THIGH_POS_Y
            )
        self.left_thigh.setheading(const.THIGH_HEADING)
        self.left_calf.goto(
            const.CALF_POS_X * self.direction_term,
            const.CALF_POS_Y
            )
        self.left_calf.setheading(const.CALF_HEADING)
        self.left_foot.goto(
            const.FOOT_POS_X * self.direction_term,
            const.FOOT_POS_Y
            )
        self.left_foot.setheading(const.FOOT_HEADING)
        self.right_thigh.goto(
            const.THIGH_POS_X * self.direction_term,
            const.THIGH_POS_Y
            )
        self.right_thigh.setheading(const.THIGH_HEADING)
        self.right_calf.goto(
            const.CALF_POS_X * self.direction_term,
            const.CALF_POS_Y
            )
        self.right_calf.setheading(const.CALF_HEADING)
        self.right_foot.goto(
            const.FOOT_POS_X * self.direction_term,
            const.FOOT_POS_Y
            )
        self.right_foot.setheading(const.FOOT_HEADING)
        self.left_upperarm.goto(
            const.UPPERARM_POS_X * self.direction_term,
            const.UPPERARM_POS_Y
            )
        self.left_upperarm.setheading(const.UPPERARM_HEADING)
        self.left_forearm.goto(
            const.FOREARM_POS_X * self.direction_term,
            const.FOREARM_POS_Y
            )
        self.left_forearm.setheading(const.FOREARM_HEADING)
        self.left_hand.goto(
            const.HAND_POS_X * self.direction_term,
            const.HAND_POS_Y
            )
        self.left_hand.setheading(const.HAND_HEADING)
        self.right_upperarm.goto(
            const.UPPERARM_POS_X * self.direction_term,
            const.UPPERARM_POS_Y
            )
        self.right_upperarm.setheading(const.UPPERARM_HEADING)
        self.right_forearm.goto(
            const.FOREARM_POS_X * self.direction_term,
            const.FOREARM_POS_Y
            )
        self.right_forearm.setheading(const.FOREARM_HEADING)
        self.right_hand.goto(
            const.HAND_POS_X * self.direction_term,
            const.HAND_POS_Y
            )
        self.right_hand.setheading(const.HAND_HEADING)

        ## Set angles to start positions.
        self.left_thigh_angle = const.THIGH_HEADING
        self.right_thigh_angle = const.THIGH_HEADING
