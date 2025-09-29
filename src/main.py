import turtle
import time
from control.Game import Game
from components.Info import Info
from components.Background import Background
from components.Surface import Surface
from components.Humanoid import Humanoid
from components.Box import Box
from utils import constants as const
from utils.helpers import direction_term
from utils.helpers import print_message


class UserInterface:
    """The game's user interface."""

    def __init__(self):
        """Initialize the user interface components"""
        self.screen = turtle.Screen()
        self.screen.setup(const.SCREEN_WID, const.SCREEN_HGT)
        self.screen.title("Humanoid Worker")
        self.screen.tracer(const.SCREEN_TRA)
        self.screen.listen()
        self.game = Game()
        self.info = Info()
        self.background = Background()
        self.surface = Surface()
        self.humanoid = Humanoid()
        self.prepare()
        print_message(self.game.exit_message)

    def start_moving(self):
        """Start humanoid moving."""
        self.humanoid.move = True

    def stop_moving(self):
        """Stop humanoid moving."""
        self.humanoid.move = False
        self.humanoid.humanoid_speed = self.humanoid.move_speed["default"]
        self.humanoid.to_start_pos()

    def faster_moving(self):
        """Change humanoid moving speed to faster."""
        if self.humanoid.humanoid_speed == self.humanoid.move_speed["default"]:
            self.humanoid.humanoid_speed = self.humanoid.move_speed["slow"]
        elif self.humanoid.humanoid_speed == self.humanoid.move_speed["slow"]:
            self.humanoid.humanoid_speed = self.humanoid.move_speed["normal"]
        elif self.humanoid.humanoid_speed ==\
                self.humanoid.move_speed["normal"]:
            self.humanoid.humanoid_speed = self.humanoid.move_speed["fast"]

    def slower_moving(self):
        """Change humanoid moving speed to slower."""
        if self.humanoid.humanoid_speed == self.humanoid.move_speed["fast"]:
            self.humanoid.humanoid_speed = self.humanoid.move_speed["normal"]
        elif self.humanoid.humanoid_speed ==\
                self.humanoid.move_speed["normal"]:
            self.humanoid.humanoid_speed = self.humanoid.move_speed["slow"]
        elif self.humanoid.humanoid_speed == self.humanoid.move_speed["slow"]:
            self.stop_moving()

    def to_left(self):
        """Change moving speed or turn to left."""
        # Start left
        if not self.humanoid.move and self.humanoid.left:
            self.faster_moving()
            self.start_moving()
        # Turn left
        elif not self.humanoid.move and self.humanoid.right:
            self.humanoid.right = False
            self.humanoid.left = True
            self.background.right = True
            self.background.left = False
            self.humanoid.to_start_pos()
            self.screen.update()
        # Faster left
        elif self.humanoid.move and self.humanoid.left:
            self.faster_moving()
        # Slower right
        elif self.humanoid.move and self.humanoid.right:
            self.slower_moving()

    def to_right(self):
        """Change moving speed or turn to right."""
        # Start right
        if not self.humanoid.move and self.humanoid.right:
            self.faster_moving()
            self.start_moving()
        # Turn right
        elif not self.humanoid.move and self.humanoid.left:
            self.humanoid.right = True
            self.humanoid.left = False
            self.background.right = False
            self.background.left = True
            self.humanoid.to_start_pos()
            self.screen.update()
        # Faster right
        elif self.humanoid.move and self.humanoid.right:
            self.faster_moving()
        # Slower left
        elif self.humanoid.move and self.humanoid.left:
            self.slower_moving()

    def wait_for_input(self):
        """Wait for user to press a key."""
        self.screen.onkeypress(self.to_left, "Left")
        self.screen.onkeypress(self.to_right, "Right")

    def prepare(self):
        """Prepare the game for running."""
        self.wait_for_input()
        self.humanoid.update_limbs()
        self.humanoid.to_start_pos()
        self.background.update_background()
        self.screen.update()

    def animate_humanoid_move(self):
        """Animate humanoid movement."""
        self.humanoid.update_limbs()
        self.background.update_background()

    def enter_factory(self):
        """Humanoid enters the factory."""
        return self.background.background_conveyor.xcor() ==\
                const.FACTORY_LEFT_END\
                    or self.background.background_conveyor.xcor() ==\
                        const.FACTORY_RIGHT_END

    def box_type(self):
        """Store box type for further use."""
        x = const.CONST_X
        y = const.CONST_Y
        if self.game.boxes[self.game.box_index].box.shapesize() ==\
                const.BOX_LIGHT_SHAPESIZE:
            self.game.box_shape = const.CONST_LIGHT
        elif self.game.boxes[self.game.box_index].box.shapesize() ==\
                const.BOX_REGULAR_SHAPESIZE:
            self.game.box_shape = const.CONST_REGULAR
        elif self.game.boxes[self.game.box_index].box.shapesize() ==\
                const.BOX_HEAVY_SHAPESIZE:
            self.game.box_shape = const.CONST_HEAVY
        self.game.box_carry_pos_x =\
            self.game.box_carry_positions[self.game.box_shape][x]
        self.game.box_carry_pos_y =\
            self.game.box_carry_positions[self.game.box_shape][y]
        self.game.box_trans_pos_x =\
            self.game.box_transport_positions[self.game.box_shape][x]
        self.game.box_trans_pos_y =\
            self.game.box_transport_positions[self.game.box_shape][y]

    def create_crate(self):
        """Create a new crate."""
        box = Box()
        self.game.boxes.append(box)
        self.game.box_index += 1
        self.game.boxes[self.game.box_index].new_box()
        self.box_type()
        self.game.create_box = False
        self.game.created_box = True

    def crate_on_conveyor_lift(self):
        """Crate is on the conveyor lift."""
        self.game.boxes[self.game.box_index].box.goto(
            self.background.conveyor_lift.xcor(),
            self.background.conveyor_lift.ycor() + self.game.box_trans_pos_y
        )

    def run(self):
        """Main loop that runs the self.game."""
        self.game.game_on = True
        self.game.create_box = True

        try:
            while self.game.game_on:
                if self.humanoid.move:
                    self.animate_humanoid_move()

                if self.background.is_conveyor_lift_down\
                    and self.game.create_box\
                        and not self.game.carrying_box\
                            and not self.game.ready_pickup:
                    if self.enter_factory():
                        self.create_crate()

                if self.game.created_box:
                    self.game.conveyor_lift_up = True

                if self.game.conveyor_lift_up:
                    self.crate_on_conveyor_lift()
                    self.background.conveyor_lift_to_up()

                if self.background.is_conveyor_lift_up:
                    self.game.conveyor_lift_up = False
                    self.game.created_box = False
                    self.game.box_left = True

                if self.game.box_left:
                    self.game.boxes[self.game.box_index].box_to_left(
                        self.background.conveyor_drive.xcor(),
                        self.humanoid.right
                    )
                    if self.game.boxes[self.game.box_index].is_box_pickup:
                        self.game.box_left = False
                        self.game.conveyor_lift_down = True
                        self.game.ready_pickup = True

                if self.game.conveyor_lift_down:
                    self.background.conveyor_lift_to_down()

                if self.background.is_conveyor_lift_down:
                    self.game.conveyor_lift_down = False

                if self.game.ready_pickup:
                    self.game.boxes[self.game.box_index].box_pickup(
                        self.background.conveyor_drive.xcor()
                    )
                    if self.game.boxes[self.game.box_index].box.xcor() == 0:
                        self.game.ready_pickup = False
                        self.game.carrying_box = True

                if self.game.carrying_box:
                    self.humanoid.hands_to_carry()
                    self.game.boxes[self.game.box_index].box.goto(
                        self.game.box_carry_pos_x * direction_term(
                            self.humanoid.left,
                            self.humanoid.right
                        ),
                        self.game.box_carry_pos_y
                    )                
                    if self.game.box_shape == const.CONST_LIGHT:
                        if self.background.light_lift.xcor() == 0:
                            self.game.carrying_box = False
                            self.game.box_in_light_lift = True
                            self.game.light_lift_up = True
                    if self.game.box_shape == const.CONST_REGULAR:
                        if self.humanoid.humanoid_speed ==\
                                self.humanoid.move_speed["fast"]:
                            self.slower_moving()
                        if self.background.regular_lift.xcor() == 0:
                            self.game.carrying_box = False
                            self.game.box_in_regular_lift = True
                            self.game.regular_lift_up = True
                    if self.game.box_shape == const.CONST_HEAVY:
                        if self.humanoid.humanoid_speed ==\
                                self.humanoid.move_speed["fast"]\
                            or self.humanoid.humanoid_speed ==\
                                self.humanoid.move_speed["normal"]:
                            self.slower_moving()
                        if self.background.heavy_lift.xcor() == 0:
                            self.game.carrying_box = False
                            self.game.box_in_heavy_lift = True
                            self.game.heavy_lift_up = True

                if self.game.box_in_light_lift:
                    self.game.boxes[self.game.box_index].box.goto(
                        self.background.light_lift.xcor(),
                        self.background.light_lift.ycor()\
                            + const.LIGHT_TRANSPORT_Y
                    )

                if self.game.box_in_regular_lift:
                    self.game.boxes[self.game.box_index].box.goto(
                        self.background.regular_lift.xcor(),
                        self.background.regular_lift.ycor()\
                            + const.REGULAR_TRANSPORT_Y
                    )

                if self.game.box_in_heavy_lift:
                    self.game.boxes[self.game.box_index].box.goto(
                        self.background.heavy_lift.xcor(),
                        self.background.heavy_lift.ycor()\
                            + const.HEAVY_TRANSPORT_Y
                    )

                if self.game.light_lift_up:
                    self.background.light_lift_to_up()

                if self.game.regular_lift_up:
                    self.background.regular_lift_to_up()

                if self.game.heavy_lift_up:
                    self.background.heavy_lift_to_up()

                if self.background.is_light_lift_up:
                    self.game.boxes[self.game.box_index].box.goto(
                        self.background.light_lift.xcor(),
                        const.LIGHT_LIFT_MAX_Y + self.game.box_trans_pos_y
                    )
                    self.game.box_in_light_lift = False
                    self.game.light_lift_up = False
                    self.game.light_lift_down = True

                if self.game.light_lift_down:
                    self.background.light_lift_to_down()

                if self.background.is_light_lift_down\
                        and not self.game.carrying_box:
                    self.game.light_lift_down = False
                    self.game.create_box = True

                if self.background.is_regular_lift_up:
                    self.game.boxes[self.game.box_index].box.goto(
                        self.background.regular_lift.xcor(),
                        const.REGULAR_LIFT_MAX_Y + self.game.box_trans_pos_y
                    )
                    self.game.box_in_regular_lift = False
                    self.game.regular_lift_up = False
                    self.game.regular_lift_down = True

                if self.game.regular_lift_down:
                    self.background.regular_lift_to_down()

                if self.background.is_regular_lift_down\
                        and not self.game.carrying_box:
                    self.game.regular_lift_down = False
                    self.game.create_box = True

                if self.background.is_heavy_lift_up:
                    self.game.boxes[self.game.box_index].box.goto(
                        self.background.heavy_lift.xcor(),
                        const.HEAVY_LIFT_MAX_Y + self.game.box_trans_pos_y
                    )
                    self.game.box_in_heavy_lift = False
                    self.game.heavy_lift_up = False
                    self.game.heavy_lift_down = True

                if self.game.heavy_lift_down:
                    self.background.heavy_lift_to_down()

                if self.background.is_heavy_lift_down\
                        and not self.game.carrying_box:
                    self.game.heavy_lift_down = False
                    self.game.create_box = True
    
                time.sleep(self.humanoid.humanoid_speed)
                self.screen.update()

        except Exception as e:
            print_message(e)

if __name__ == "__main__":
    user_interface = UserInterface()
    user_interface.run()
