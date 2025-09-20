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
            # Humanoid carries box allowed
            if ((background.conveyor_drive_xcor >= 0\
                 and background.conveyor_drive_xcor <= 45)\
                or (background.conveyor_drive_xcor <= 0\
                    and background.conveyor_drive_xcor >= -45))\
                and (background.conveyor_trackpoint.xcor() ==\
                     background._background_conveyor_pos_x\
                        + const.CONVEYOR_LIFT_POS_X - 500):
                if humanoid.move:
                    humanoid.carries_box = True
                    background.conveyor_lift_up = False
                    background.conveyor_lift_down = True
            # Humanoid carries box left and right
            if humanoid.carries_box:
                background.trackpoint_stop = False
                background.trackpoint_to_left = False
                background.update_conveyor_lift()
                # Hide trackpoint
                background.conveyor_trackpoint.goto(0, 0)
                # Change box position relative to hands and humanoid speed
                if background.boxes[background.box_index].box.shapesize() ==\
                    const.BOX_LIGHT_SHAPESIZE:
                    if humanoid.right:
                        background.boxes[background.box_index]\
                            .update_box(30, 30)
                    if humanoid.left:
                        background.boxes[background.box_index]\
                            .update_box(-30, 30)
                if background.boxes[background.box_index].box.shapesize() ==\
                    const.BOX_REGULAR_SHAPESIZE:
                    if humanoid.humanoid_speed == humanoid.move_speed["fast"]:
                        slower_moving()
                    if humanoid.right:
                        background.boxes[background.box_index]\
                            .update_box(35, 30)
                    if humanoid.left:
                        background.boxes[background.box_index]\
                            .update_box(-35, 30)
                if background.boxes[background.box_index].box.shapesize() ==\
                    const.BOX_HEAVY_SHAPESIZE:
                    if humanoid.humanoid_speed ==\
                        humanoid.move_speed["fast"]\
                        or humanoid.humanoid_speed ==\
                        humanoid.move_speed["normal"]:
                        slower_moving()
                    if humanoid.right:
                        background.boxes[background.box_index]\
                            .update_box(45, 30)
                    if humanoid.left:
                        background.boxes[background.box_index]\
                            .update_box(-45, 30)
                # Light lift hoist
                if background.boxes[background.box_index].box.shapesize() ==\
                    const.BOX_LIGHT_SHAPESIZE\
                    and background.light_lift_xcor == 0:
                    humanoid.carries_box = False
                    background.light_lift_move = True
                    background.light_lift_up = True
                    background.box_is_hoisted = True
                # Regular lift hoist
                if background.boxes[background.box_index].box.shapesize() ==\
                    const.BOX_REGULAR_SHAPESIZE\
                    and background.regular_lift_xcor == 0:
                    humanoid.carries_box = False
                    background.regular_lift_move = True
                    background.regular_lift_up = True
                    background.box_is_hoisted = True
                # Heavy lift hoist
                if background.boxes[background.box_index].box.shapesize() ==\
                    const.BOX_HEAVY_SHAPESIZE\
                    and background.heavy_lift_xcor == 0:
                    humanoid.carries_box = False
                    background.heavy_lift_move = True
                    background.heavy_lift_up = True
                    background.box_is_hoisted = True
            # Box in light lift
            if not humanoid.carries_box\
                and background.light_lift_move\
                    and background.light_lift_up\
                        and background.box_is_hoisted:
                # Box above screen
                if (background.light_lift.ycor() >=\
                    const.LIGHT_LIFT_MAX_Y - 1)\
                    and not background.box_is_delivered:
                    background.boxes[background.box_index].box.goto(0, 500)
                    box = Box()
                    background.boxes.append(box)
                    background.box_index += 1
                    background.boxes[background.box_index].new_box()
                    background.box_is_delivered = True
                else:
                    background.boxes[background.box_index].update_box(
                        background.light_lift.xcor(),
                        background.light_lift.ycor()
                        )
            # Box in regular lift
            if not humanoid.carries_box\
                and background.regular_lift_move\
                    and background.regular_lift_up\
                        and background.box_is_hoisted:
                # Box above screen
                if (background.regular_lift.ycor() >=\
                    const.REGULAR_LIFT_MAX_Y - 1)\
                    and not background.box_is_delivered:
                    background.boxes[background.box_index].box.goto(0, 500)
                    box = Box()
                    background.boxes.append(box)
                    background.box_index += 1
                    background.boxes[background.box_index].new_box()
                    background.box_is_delivered = True
                else:
                    background.boxes[background.box_index].update_box(
                        background.regular_lift.xcor(),
                        background.regular_lift.ycor()
                        )
            # Box in heavy lift
            if not humanoid.carries_box\
                and background.heavy_lift_move\
                    and background.heavy_lift_up\
                        and background.box_is_hoisted:
                # Box above screen
                if (background.heavy_lift.ycor() >=\
                    const.HEAVY_LIFT_MAX_Y - 1)\
                    and not background.box_is_delivered:
                    background.boxes[background.box_index].box.goto(0, 500)
                    box = Box()
                    background.boxes.append(box)
                    background.box_index += 1
                    background.boxes[background.box_index].new_box()
                    background.box_is_delivered = True
                else:
                    background.boxes[background.box_index].update_box(
                        background.heavy_lift.xcor(),
                        background.heavy_lift.ycor()
                        )
            # Humanoid is moving
            if humanoid.move:
                humanoid.update_limbs()
                background.update_background()
            # Trackpoint moves to left when humanoid moves to right
            if background.trackpoint_to_left:
                background.conveyor_trackpoint_to_left()
                background.boxes[background.box_index].update_box(
                    background.conveyor_trackpoint.xcor(),
                    background.conveyor_trackpoint.ycor()
                    )
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
            if background.conveyor_lift_move and not humanoid.carries_box:
                background.update_conveyor_lift()
                background.boxes[background.box_index].update_box(
                    background.conveyor_trackpoint.xcor(),
                    background.conveyor_trackpoint.ycor()
                    )
                background.update_conveyor_trackpoint()
            # Conveyor trackpoint allowed to left
            if not background.conveyor_lift_move\
                and not background.trackpoint_stop\
                    and not humanoid.carries_box\
                        and not background.box_is_hoisted:
                background.trackpoint_to_left = True
                background.check_if_ready()
            # Conveyor trackpoint moves to left
            if background.trackpoint_to_left\
                and not background.trackpoint_stop:
                background.conveyor_trackpoint_to_left()
                background.boxes[background.box_index].update_box(
                    background.conveyor_trackpoint.xcor(),
                    background.conveyor_trackpoint.ycor()
                    )
            # Conveyor trackpoint stop
            if not background.conveyor_lift_move\
                and not background.trackpoint_to_left\
                    and not humanoid.carries_box\
                        and not background.box_is_hoisted:
                background.trackpoint_stop = True
                background.conveyor_trackpoint.goto(
                    background._background_conveyor_pos_x\
                        + const.CONVEYOR_LIFT_POS_X - 500,
                    background.conveyor_trackpoint.ycor()
                )
                background.boxes[background.box_index].update_box(
                    background.conveyor_trackpoint.xcor(),
                    background.conveyor_trackpoint.ycor()
                    )

            time.sleep(humanoid.humanoid_speed)
            screen.update()
    except Exception as e:
        print(e)
        # pass

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
    background.boxes[background.box_index].update_box(
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
    box = Box()
    background.boxes.append(box)
    background.boxes[background.box_index].new_box()
    humanoid = Humanoid()
    print(box.box.shapesize())

    start()
