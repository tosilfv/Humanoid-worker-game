import turtle
import time
from control.game import Game
from components.info import Info
from components.background import Background
from components.surface import Surface
from components.humanoid import Humanoid
from components.box import Box
from utils.helpers import direction_term
from utils.helpers import print_message
import utils.constants as const

screen = turtle.Screen()
screen.setup(const.SCREEN_WID, const.SCREEN_HGT)
screen.title("Humanoid Worker")
screen.tracer(const.SCREEN_TRA)
screen.listen()

def start_moving():
    """Start humanoid moving."""
    humanoid.move = True

def stop_moving():
    """Stop humanoid moving."""
    humanoid.move = False
    humanoid.humanoid_speed = humanoid.move_speed["default"]
    humanoid.to_start_pos()

def faster_moving():
    """Change humanoid moving speed to faster."""
    if humanoid.humanoid_speed == humanoid.move_speed["default"]:
        humanoid.humanoid_speed = humanoid.move_speed["slow"]
    elif humanoid.humanoid_speed == humanoid.move_speed["slow"]:
        humanoid.humanoid_speed = humanoid.move_speed["normal"]
    elif humanoid.humanoid_speed == humanoid.move_speed["normal"]:
        humanoid.humanoid_speed = humanoid.move_speed["fast"]

def slower_moving():
    """Change humanoid moving speed to slower."""
    if humanoid.humanoid_speed == humanoid.move_speed["fast"]:
        humanoid.humanoid_speed = humanoid.move_speed["normal"]
    elif humanoid.humanoid_speed == humanoid.move_speed["normal"]:
        humanoid.humanoid_speed = humanoid.move_speed["slow"]
    elif humanoid.humanoid_speed == humanoid.move_speed["slow"]:
        stop_moving()

def to_left():
    """Change moving speed or turn to left."""
    # Start left
    if not humanoid.move and humanoid.left:
        faster_moving()
        start_moving()
    # Turn left
    elif not humanoid.move and humanoid.right:
        humanoid.right = False
        humanoid.left = True
        background.right = True
        background.left = False
        humanoid.to_start_pos()
        screen.update()
    # Faster left
    elif humanoid.move and humanoid.left:
        faster_moving()
    # Slower right
    elif humanoid.move and humanoid.right:
        slower_moving()

def to_right():
    """Change moving speed or turn to right."""
    # Start right
    if not humanoid.move and humanoid.right:
        faster_moving()
        start_moving()
    # Turn right
    elif not humanoid.move and humanoid.left:
        humanoid.right = True
        humanoid.left = False
        background.right = False
        background.left = True
        humanoid.to_start_pos()
        screen.update()
    # Faster right
    elif humanoid.move and humanoid.right:
        faster_moving()
    # Slower left
    elif humanoid.move and humanoid.left:
        slower_moving()

def wait_for_input():
    """Wait for user to press a key."""
    screen.onkeypress(to_left, "Left")
    screen.onkeypress(to_right, "Right")

def prepare():
    """Prepare the game for running."""
    wait_for_input()
    humanoid.update_limbs()
    humanoid.to_start_pos()
    background.update_background()
    screen.update()
    run()

def animate_humanoid_move():
    """Animate humanoid movement."""
    humanoid.update_limbs()
    background.update_background()

def enter_factory():
    """Humanoid enters the factory."""
    return background.background_conveyor.xcor() ==\
            const.FACTORY_LEFT_END\
                or background.background_conveyor.xcor() ==\
                    const.FACTORY_RIGHT_END

def box_type():
    """Store box type for further use."""
    x = const.CONST_X
    y = const.CONST_Y
    if game.boxes[game.box_index].box.shapesize() ==\
            const.BOX_LIGHT_SHAPESIZE:
        game.box_shape = const.CONST_LIGHT
    elif game.boxes[game.box_index].box.shapesize() ==\
            const.BOX_REGULAR_SHAPESIZE:
        game.box_shape = const.CONST_REGULAR
    elif game.boxes[game.box_index].box.shapesize() ==\
            const.BOX_HEAVY_SHAPESIZE:
        game.box_shape = const.CONST_HEAVY
    game.box_carry_pos_x = game.box_carry_positions[game.box_shape][x]
    game.box_carry_pos_y = game.box_carry_positions[game.box_shape][y]
    game.box_trans_pos_x = game.box_transport_positions[game.box_shape][x]
    game.box_trans_pos_y = game.box_transport_positions[game.box_shape][y]

def create_crate():
    """Create a new crate."""
    box = Box()
    game.boxes.append(box)
    game.box_index += 1
    game.boxes[game.box_index].new_box()
    box_type()
    game.create_box = False
    game.created_box = True

def crate_on_conveyor_lift():
    """Crate is on the conveyor lift."""
    game.boxes[game.box_index].box.goto(
        background.conveyor_lift.xcor(),
        background.conveyor_lift.ycor() + game.box_trans_pos_y
    )

def run():
    """Main loop that runs the game."""
    game.game_on = True
    game.create_box = True

    try:
        while game.game_on:
            if humanoid.move:
                animate_humanoid_move()

            if background.is_conveyor_lift_down\
                and game.create_box\
                    and not game.carrying_box\
                        and not game.ready_pickup:
                if enter_factory():
                    create_crate()

            if game.created_box:
                game.conveyor_lift_up = True

            if game.conveyor_lift_up:
                crate_on_conveyor_lift()
                background.conveyor_lift_to_up()

            if background.is_conveyor_lift_up:
                game.conveyor_lift_up = False
                game.created_box = False
                game.box_left = True

            if game.box_left:
                game.boxes[game.box_index].box_to_left(
                    background.conveyor_drive.xcor(),
                    humanoid.right
                )
                if game.boxes[game.box_index].is_box_pickup:
                    game.box_left = False
                    game.conveyor_lift_down = True
                    game.ready_pickup = True

            if game.conveyor_lift_down:
                background.conveyor_lift_to_down()

            if background.is_conveyor_lift_down:
                game.conveyor_lift_down = False

            if game.ready_pickup:
                game.boxes[game.box_index].box_pickup(
                    background.conveyor_drive.xcor()
                )
                if game.boxes[game.box_index].box.xcor() == 0:
                    game.ready_pickup = False
                    game.carrying_box = True

            if game.carrying_box:
                humanoid.hands_to_carry()
                game.boxes[game.box_index].box.goto(
                    game.box_carry_pos_x * direction_term(
                        humanoid.left,
                        humanoid.right
                    ),
                    game.box_carry_pos_y
                )                
                if game.box_shape == const.CONST_LIGHT:
                    if background.light_lift.xcor() == 0:
                        game.carrying_box = False
                        game.box_in_light_lift = True
                        game.light_lift_up = True
                if game.box_shape == const.CONST_REGULAR:
                    if humanoid.humanoid_speed == humanoid.move_speed["fast"]:
                        slower_moving()
                    if background.regular_lift.xcor() == 0:
                        game.carrying_box = False
                        game.box_in_regular_lift = True
                        game.regular_lift_up = True
                if game.box_shape == const.CONST_HEAVY:
                    if humanoid.humanoid_speed == humanoid.move_speed["fast"]\
                        or humanoid.humanoid_speed ==\
                            humanoid.move_speed["normal"]:
                        slower_moving()
                    if background.heavy_lift.xcor() == 0:
                        game.carrying_box = False
                        game.box_in_heavy_lift = True
                        game.heavy_lift_up = True

            if game.box_in_light_lift:
                game.boxes[game.box_index].box.goto(
                    background.light_lift.xcor(),
                    background.light_lift.ycor() + const.LIGHT_TRANSPORT_Y
                )

            if game.box_in_regular_lift:
                game.boxes[game.box_index].box.goto(
                    background.regular_lift.xcor(),
                    background.regular_lift.ycor() + const.REGULAR_TRANSPORT_Y
                )

            if game.box_in_heavy_lift:
                game.boxes[game.box_index].box.goto(
                    background.heavy_lift.xcor(),
                    background.heavy_lift.ycor() + const.HEAVY_TRANSPORT_Y
                )

            if game.light_lift_up:
                background.light_lift_to_up()

            if game.regular_lift_up:
                background.regular_lift_to_up()

            if game.heavy_lift_up:
                background.heavy_lift_to_up()

            if background.is_light_lift_up:
                game.boxes[game.box_index].box.goto(
                    background.light_lift.xcor(),
                    const.LIGHT_LIFT_MAX_Y + game.box_trans_pos_y
                )
                game.box_in_light_lift = False
                game.light_lift_up = False
                game.light_lift_down = True

            if game.light_lift_down:
                background.light_lift_to_down()

            if background.is_light_lift_down and not game.carrying_box:
                game.light_lift_down = False
                game.create_box = True

            if background.is_regular_lift_up:
                game.boxes[game.box_index].box.goto(
                    background.regular_lift.xcor(),
                    const.REGULAR_LIFT_MAX_Y + game.box_trans_pos_y
                )
                game.box_in_regular_lift = False
                game.regular_lift_up = False
                game.regular_lift_down = True

            if game.regular_lift_down:
                background.regular_lift_to_down()

            if background.is_regular_lift_down and not game.carrying_box:
                game.regular_lift_down = False
                game.create_box = True

            if background.is_heavy_lift_up:
                game.boxes[game.box_index].box.goto(
                    background.heavy_lift.xcor(),
                    const.HEAVY_LIFT_MAX_Y + game.box_trans_pos_y
                )
                game.box_in_heavy_lift = False
                game.heavy_lift_up = False
                game.heavy_lift_down = True

            if game.heavy_lift_down:
                background.heavy_lift_to_down()

            if background.is_heavy_lift_down and not game.carrying_box:
                game.heavy_lift_down = False
                game.create_box = True
 
            time.sleep(humanoid.humanoid_speed)
            screen.update()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    game = Game()
    info = Info()
    background = Background()
    surface = Surface()
    humanoid = Humanoid()
    prepare()
    print_message(game.exit_message)
