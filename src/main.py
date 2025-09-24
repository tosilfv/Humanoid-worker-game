import turtle
import time
from control.game import Game
from components.info import Info
from components.background import Background
from components.surface import Surface
from components.humanoid import Humanoid
from components.box import Box
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

def create_crate():
    """Create a new crate."""
    box = Box()
    game.boxes.append(box)
    game.boxes[game.box_index].new_box()
    game.create_box = False
    game.created_box = True

def crate_on_conveyor_lift():
    """Crate is on the conveyor lift."""
    game.boxes[game.box_index].box.goto(
        background.conveyor_lift.xcor(),
        background.conveyor_lift.ycor()
    )

def run():
    """Main loop that runs the game."""
    game.game_on = True
    game.create_box = True

    try:
        while game.game_on:
            if humanoid.move:
                animate_humanoid_move()

            if game.create_box:
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
                game.boxes[game.box_index].box_to_left(humanoid.right)
                if game.boxes[game.box_index].is_box_pickup:
                    game.box_left = False
                    game.ready_pickup = True

            if game.ready_pickup:
                game.boxes[game.box_index].box_pickup(
                    background.background_conveyor.xcor()
                )

            time.sleep(humanoid.humanoid_speed)
            screen.update()

    except Exception:
        pass

if __name__ == "__main__":
    game = Game()
    info = Info()
    background = Background()
    surface = Surface()
    humanoid = Humanoid()
    prepare()
    print_message(game.exit_message)


























































































# # Humanoid Worker Game

# import turtle
# import time
# import utils.constants as const
# from components.background import Background
# from components.box import Box
# from components.humanoid import Humanoid
# from components.info import Info
# from components.surface import Surface

# screen = turtle.Screen()
# screen.setup(const.SCREEN_WID, const.SCREEN_HGT)
# screen.title("Humanoid Worker")
# screen.tracer(const.SCREEN_TRA)
# screen.listen()

# def box_follows_trackpoint():
#     """Box follows trackpoint."""
#     background.boxes[background.box_index].update_box(
#         background.trackpoint.xcor(),
#         background.trackpoint.ycor()
#         )

# def go():
#     """Main loop to keep humanoid moving."""

#     try:
#         while True:

#             # Humanoid moves
#             if humanoid.move:
#                 humanoid.update_limbs()
#                 background.update_background()

#             # Light lift moves
#             if background.light_lift_move:
#                 background.update_light_lift()
#             # Regular lift moves
#             if background.regular_lift_move:
#                 background.update_regular_lift()
#             # Heavy lift moves
#             if background.heavy_lift_move:
#                 background.update_heavy_lift()

#             # Trackpoint allowed to left
#             if not background.conveyor_lift_move and not humanoid.carries_box:
#                 background.trackpoint_left = True
#                 background.stop_at_pickup()

#             # Trackpoint moves to left
#             if background.trackpoint_left:
#                 background.trackpoint_to_left()
#                 box_follows_trackpoint()
#                 background.trackpoint_to_left()
#                 box_follows_trackpoint()

#             # Trackpoint stops at conveyor pick up point
#             if not background.conveyor_lift_move and not humanoid.carries_box and not background.trackpoint_left:
#                 background.trackpoint.goto(
#                     background.background_conveyor.xcor() + const.CONVEYOR_LIFT_POS_X + const.BOX_PICKUP_POS_X,
#                     background.trackpoint.ycor()
#                 )
#                 box_follows_trackpoint()

#             # Conveyor lift moves
#             if background.conveyor_lift_move and not humanoid.carries_box:
#                 background.update_conveyor_lift()
#                 box_follows_trackpoint()
#                 background.update_trackpoint()

#             # Humanoid carries box allowed
#             if ((background.conveyor_drive.xcor() >= 0 and background.conveyor_drive.xcor() <= 45)\
#                 or (background.conveyor_drive.xcor() <= 0 and background.conveyor_drive.xcor() >= -45))\
#                 and (background.trackpoint.xcor() == background.background_conveyor.xcor() + const.CONVEYOR_LIFT_POS_X + const.BOX_PICKUP_POS_X):
#                 if humanoid.move:
#                     humanoid.carries_box = True
#                     background.conveyor_lift_up = False
#                     background.conveyor_lift_down = True

#             # Humanoid carries box left and right
#             if humanoid.carries_box:
#                 background.trackpoint_left = False
#                 background.update_conveyor_lift()
#                 # Hide trackpoint
#                 background.trackpoint.goto(0, 0)
#                 # Change box position relative to hands and humanoid speed
#                 if background.boxes[background.box_index].box.shapesize() == const.BOX_LIGHT_SHAPESIZE:
#                     if humanoid.right:
#                         background.boxes[background.box_index].update_box(30, 30)
#                     if humanoid.left:
#                         background.boxes[background.box_index].update_box(-30, 30)
#                 if background.boxes[background.box_index].box.shapesize() == const.BOX_REGULAR_SHAPESIZE:
#                     if humanoid.humanoid_speed == humanoid.move_speed["fast"]:
#                         slower_moving()
#                     if humanoid.right:
#                         background.boxes[background.box_index].update_box(35, 30)
#                     if humanoid.left:
#                         background.boxes[background.box_index].update_box(-35, 30)
#                 if background.boxes[background.box_index].box.shapesize() == const.BOX_HEAVY_SHAPESIZE:
#                     if humanoid.humanoid_speed == humanoid.move_speed["fast"] or humanoid.humanoid_speed == humanoid.move_speed["normal"]:
#                         slower_moving()
#                     if humanoid.right:
#                         background.boxes[background.box_index].update_box(45, 30)
#                     if humanoid.left:
#                         background.boxes[background.box_index].update_box(-45, 30)

#                 # Light lift hoist
#                 if background.boxes[background.box_index].box.shapesize() == const.BOX_LIGHT_SHAPESIZE and background.light_lift.xcor() == 0:
#                     humanoid.carries_box = False
#                     background.light_lift_move = True
#                     background.light_lift_up = True
#                     background.box_is_hoisted = True
#                 # Regular lift hoist
#                 if background.boxes[background.box_index].box.shapesize() == const.BOX_REGULAR_SHAPESIZE and background.regular_lift.xcor() == 0:
#                     humanoid.carries_box = False
#                     background.regular_lift_move = True
#                     background.regular_lift_up = True
#                     background.box_is_hoisted = True
#                 # Heavy lift hoist
#                 if background.boxes[background.box_index].box.shapesize() == const.BOX_HEAVY_SHAPESIZE and background.heavy_lift.xcor() == 0:
#                     humanoid.carries_box = False
#                     background.heavy_lift_move = True
#                     background.heavy_lift_up = True
#                     background.box_is_hoisted = True

#             # Box in light lift
#             if not humanoid.carries_box and background.light_lift_move and background.light_lift_up and background.box_is_hoisted:
#                 # Box above screen
#                 if (background.light_lift.ycor() >= const.LIGHT_LIFT_MAX_Y - 1) and not background.box_is_delivered:
#                     background.boxes[background.box_index].box.goto(const.BOX_ABOVE_SCREEN_POS_X, const.BOX_ABOVE_SCREEN_POS_Y)
#                     box = Box()
#                     background.boxes.append(box)
#                     background.box_index += 1
#                     background.boxes[background.box_index].new_box()
#                     background.box_is_delivered = True
#                 else:
#                     background.boxes[background.box_index].update_box(
#                         background.light_lift.xcor(),
#                         background.light_lift.ycor()
#                         )
#             # Box in regular lift
#             if not humanoid.carries_box and background.regular_lift_move and background.regular_lift_up and background.box_is_hoisted:
#                 # Box above screen
#                 if (background.regular_lift.ycor() >= const.REGULAR_LIFT_MAX_Y - 1) and not background.box_is_delivered:
#                     background.boxes[background.box_index].box.goto(const.BOX_ABOVE_SCREEN_POS_X, const.BOX_ABOVE_SCREEN_POS_Y)
#                     box = Box()
#                     background.boxes.append(box)
#                     background.box_index += 1
#                     background.boxes[background.box_index].new_box()
#                     background.box_is_delivered = True
#                 else:
#                     background.boxes[background.box_index].update_box(
#                         background.regular_lift.xcor(),
#                         background.regular_lift.ycor()
#                         )
#             # Box in heavy lift
#             if not humanoid.carries_box and background.heavy_lift_move and background.heavy_lift_up and background.box_is_hoisted:
#                 # Box above screen
#                 if (background.heavy_lift.ycor() >= const.HEAVY_LIFT_MAX_Y - 1) and not background.box_is_delivered:
#                     background.boxes[background.box_index].box.goto(const.BOX_ABOVE_SCREEN_POS_X, const.BOX_ABOVE_SCREEN_POS_Y)
#                     box = Box()
#                     background.boxes.append(box)
#                     background.box_index += 1
#                     background.boxes[background.box_index].new_box()
#                     background.box_is_delivered = True
#                 else:
#                     background.boxes[background.box_index].update_box(
#                         background.heavy_lift.xcor(),
#                         background.heavy_lift.ycor()
#                         )

#             time.sleep(humanoid.humanoid_speed)
#             screen.update()
#     except Exception as e:
#         print(e)
#         # pass

# def start_moving():
#     """Start humanoid moving."""
#     humanoid.move = True

# def stop_moving():
#     """Stop humanoid moving."""
#     humanoid.move = False
#     humanoid.humanoid_speed = humanoid.move_speed["default"]
#     humanoid.to_start_pos()

# def slower_moving():
#     """Change humanoid moving speed to slower."""
#     if humanoid.humanoid_speed == humanoid.move_speed["fast"]:
#         humanoid.humanoid_speed = humanoid.move_speed["normal"]
#     elif humanoid.humanoid_speed == humanoid.move_speed["normal"]:
#         humanoid.humanoid_speed = humanoid.move_speed["slow"]
#     elif humanoid.humanoid_speed == humanoid.move_speed["slow"]:
#         stop_moving()

# def faster_moving():
#     """Change humanoid moving speed to faster."""
#     if humanoid.humanoid_speed == humanoid.move_speed["default"]:
#         humanoid.humanoid_speed = humanoid.move_speed["slow"]
#     elif humanoid.humanoid_speed == humanoid.move_speed["slow"]:
#         humanoid.humanoid_speed = humanoid.move_speed["normal"]
#     elif humanoid.humanoid_speed == humanoid.move_speed["normal"]:
#         humanoid.humanoid_speed = humanoid.move_speed["fast"]

# def to_right():
#     """Change moving speed or turn to right."""
#     # Start right
#     if not humanoid.move and humanoid.right:
#         faster_moving()
#         start_moving()
#         go()
#     # Turn right
#     elif not humanoid.move and humanoid.left:
#         humanoid.right = True
#         humanoid.left = False
#         background.right = False
#         background.left = True
#         humanoid.to_start_pos()
#         screen.update()
#     # Faster right
#     elif humanoid.move and humanoid.right:
#         faster_moving()
#     # Slower left
#     elif humanoid.move and humanoid.left:
#         slower_moving()

# def to_left():
#     """Change moving speed or turn to left."""
#     # Start left
#     if not humanoid.move and humanoid.left:
#         faster_moving()
#         start_moving()
#         go()
#     # Turn left
#     elif not humanoid.move and humanoid.right:
#         humanoid.right = False
#         humanoid.left = True
#         background.right = True
#         background.left = False
#         humanoid.to_start_pos()
#         screen.update()
#     # Faster left
#     elif humanoid.move and humanoid.left:
#         faster_moving()
#     # Slower right
#     elif humanoid.move and humanoid.right:
#         slower_moving()

# def box_to_start():
#     """Send box to start position."""
#     background.boxes[background.box_index].update_box(
#         background.conveyor_lift.xcor(),
#         background.conveyor_lift.ycor()
#         )

# def wait_for_input():
#     """Wait for user to press a key."""
#     screen.onkeypress(to_left, "Left")
#     screen.onkeypress(to_right, "Right")

# def start():
#     """Start the animation and handle screen closing."""
#     wait_for_input()
#     humanoid.update_limbs()
#     humanoid.to_start_pos()
#     background.update_background()
#     box_to_start()
#     screen.update()
#     screen.exitonclick()

# # Run the game
# if __name__ == "__main__":
#     info = Info()
#     background = Background()
#     surface = Surface()
#     box = Box()
#     background.boxes.append(box)
#     background.boxes[background.box_index].new_box()
#     humanoid = Humanoid()
#     start()
