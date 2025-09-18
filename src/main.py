# Humanoid Worker Game

import turtle
import time
import utils.constants as const
from components.humanoid import Humanoid
from components.info import Info
from components.surface import Surface
from components.background import Background
from components.box import Box

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Humanoid Worker")
screen.tracer(0)
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

def go():
    """Main loop to keep humanoid moving."""
    start_moving()

    try:
        while True:
            # Humanoid carries box
            if background.conveyor_drive_xcor == 0:
                humanoid.carries_box = True
            # Humanoid moves
            if humanoid.move:
                humanoid.update_limbs()
                background.update_background()
            # Light lift moves
            if background.light_lift_move:
                background.update_light_lift()
            # Regular lift moves
            if background.regular_lift_move:
                background.update_regular_lift()
            # Heavy lift moves
            if background.heavy_lift_move:
                background.update_heavy_lift()
            # Conveyor lift moves
            if background.conveyor_lift_move:
                background.update_conveyor_lift()
                # box.update_box(0, 0)
                box.update_box(
                    background.conveyor_lift_xcor,
                    background.conveyor_lift_ycor
                    )

            time.sleep(humanoid.humanoid_speed)
            screen.update()
    except Exception:
        pass

def to_left():
    """Change moving speed or turn to left."""
    # Start left
    if not humanoid.move and humanoid.left:
        faster_moving()
        go()
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
        go()
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

def start():
    """Start the animation and handle screen closing."""
    wait_for_input()
    humanoid.update_limbs()
    humanoid.to_start_pos()
    background.update_background()
    box.update_box(
        background.conveyor_lift_xcor,
        background.conveyor_lift_ycor
        )
    screen.update()
    screen.exitonclick()

# Create and run the game
if __name__ == "__main__":
    info = Info()
    background = Background()
    surface = Surface()
    humanoid = Humanoid()
    box = Box()
    box.new_box()
    print(box.box.shapesize())

    start()
