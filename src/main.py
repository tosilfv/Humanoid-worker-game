# Humanoid Worker Game

import turtle
import time
from humanoid import Humanoid
from info import Info
from surface import Surface
from background import Background

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
    screen.update()

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

    while humanoid.move:
        time.sleep(humanoid.humanoid_speed)
        humanoid.update_limbs()
        background.update_background()
        screen.update()

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
    screen.update()
    screen.exitonclick()

# Create and run the game
if __name__ == "__main__":
    info = Info()
    background = Background()
    surface = Surface()
    humanoid = Humanoid()
    start()
