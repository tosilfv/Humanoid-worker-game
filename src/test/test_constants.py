import unittest
from utils.constants import *


class TestConstants(unittest.TestCase):
    """Tests for * from utils/constants."""

    def test_screen_wid(self):
        self.assertEqual(SCREEN_WID, 800)

    def test_screen_hgt(self):
        self.assertEqual(SCREEN_HGT, 800)

    def test_screen_tra(self):
        self.assertEqual(SCREEN_TRA, 0)

    def test_const_x(self):
        self.assertEqual(CONST_X, "x")

    def test_const_y(self):
        self.assertEqual(CONST_Y, "y")

    def test_const_light(self):
        self.assertEqual(CONST_LIGHT, "light")

    def test_const_regular(self):
        self.assertEqual(CONST_REGULAR, "regular")

    def test_const_heavy(self):
        self.assertEqual(CONST_HEAVY, "heavy")

    def test_speed(self):
        self.assertEqual(SPEED, 0)

    def test_black(self):
        self.assertEqual(BLACK, "black")

    def test_grey(self):
        self.assertEqual(GREY, "grey")

    def test_darkgrey(self):
        self.assertEqual(DARKGREY, "darkgrey")

    def test_lightgrey(self):
        self.assertEqual(LIGHTGREY, "lightgrey")

    def test_red(self):
        self.assertEqual(RED, "red")

    def test_mahogany(self):
        self.assertEqual(MAHOGANY, "#420D09")

    def test_mocha(self):
        self.assertEqual(MOCHA, "#654321")

    def test_copper(self):
        self.assertEqual(COPPER, "#B87333")

    def test_forestgreen(self):
        self.assertEqual(FORESTGREEN, "#014421")

    def test_tropicalrainforest(self):
        self.assertEqual(TROPICALRAINFOREST, "#00755E")

    def test_midnightdenim(self):
        self.assertEqual(MIDNIGHTDENIM, "#2A3F54")

    def test_oceandenim(self):
        self.assertEqual(OCEANDENIM, "#4B5C77")

    def test_bleacheddenim(self):
        self.assertEqual(BLEACHEDDENIM, "#B0C4DE")

    def test_dayskyblue(self):
        self.assertEqual(DAYSKYBLUE, "#82CAFF")

    def test_box_light_color(self):
        self.assertEqual(BOX_LIGHT_COLOR, "#B87333")

    def test_box_regular_color(self):
        self.assertEqual(BOX_REGULAR_COLOR, "#654321")

    def test_box_heavy_color(self):
        self.assertEqual(BOX_HEAVY_COLOR, "#420D09")

    def test_arrow(self):
        self.assertEqual(ARROW, "arrow")

    def test_circle(self):
        self.assertEqual(CIRCLE, "circle")

    def test_square(self):
        self.assertEqual(SQUARE, "square")

    def test_triangle(self):
        self.assertEqual(TRIANGLE, "triangle")

    def test_font_name(self):
        self.assertEqual(FONT_NAME, "Arial")

    def test_font_size(self):
        self.assertEqual(FONT_SIZE, 16)

    def test_font_type(self):
        self.assertEqual(FONT_TYPE, "normal")

    def test_exit_message(self):
        self.assertEqual(EXIT_MESSAGE, "Thanks for playing!")

    def test_name_face(self):
        self.assertEqual(NAME_FACE, "face")

    def test_name_cranium(self):
        self.assertEqual(NAME_CRANIUM, "cranium")

    def test_name_shoulders(self):
        self.assertEqual(NAME_SHOULDERS, "shoulders")

    def test_name_chest(self):
        self.assertEqual(NAME_CHEST, "chest")

    def test_name_waist(self):
        self.assertEqual(NAME_WAIST, "waist")

    def test_name_pelvis(self):
        self.assertEqual(NAME_PELVIS, "pelvis")

    def test_name_left_thigh(self):
        self.assertEqual(NAME_LEFT_THIGH, "left_thigh")

    def test_name_left_calf(self):
        self.assertEqual(NAME_LEFT_CALF, "left_calf")

    def test_name_left_foot(self):
        self.assertEqual(NAME_LEFT_FOOT, "left_foot")

    def test_name_right_thigh(self):
        self.assertEqual(NAME_RIGHT_THIGH, "right_thigh")

    def test_name_right_calf(self):
        self.assertEqual(NAME_RIGHT_CALF, "right_calf")

    def test_name_right_foot(self):
        self.assertEqual(NAME_RIGHT_FOOT, "right_foot")

    def test_name_left_upperarm(self):
        self.assertEqual(NAME_LEFT_UPPERARM, "left_upperarm")

    def test_name_left_forearm(self):
        self.assertEqual(NAME_LEFT_FOREARM, "left_forearm")

    def test_name_left_hand(self):
        self.assertEqual(NAME_LEFT_HAND, "left_hand")

    def test_name_right_upperarm(self):
        self.assertEqual(NAME_RIGHT_UPPERARM, "right_upperarm")

    def test_name_right_forearm(self):
        self.assertEqual(NAME_RIGHT_FOREARM, "right_forearm")

    def test_name_right_hand(self):
        self.assertEqual(NAME_RIGHT_HAND, "right_hand")

    def test_default(self):
        self.assertEqual(DEFAULT, 0.0001)

    def test_slow(self):
        self.assertEqual(SLOW, 0.005)

    def test_normal(self):
        self.assertEqual(NORMAL, 0.001)

    def test_fast(self):
        self.assertEqual(FAST, 0)

    def test_zero(self):
        self.assertEqual(ZERO, 0)

    def test_face_wid(self):
        self.assertEqual(FACE_WID, 0.5)

    def test_face_len(self):
        self.assertEqual(FACE_LEN, 1.1)

    def test_cranium_wid(self):
        self.assertEqual(CRANIUM_WID, 0.9)

    def test_cranium_len(self):
        self.assertEqual(CRANIUM_LEN, 0.8)

    def test_shoulders_wid(self):
        self.assertEqual(SHOULDERS_WID, 0.4)

    def test_shoulders_len(self):
        self.assertEqual(SHOULDERS_LEN, 1)

    def test_chest_wid(self):
        self.assertEqual(CHEST_WID, 1)

    def test_chest_len(self):
        self.assertEqual(CHEST_LEN, 1)

    def test_waist_wid(self):
        self.assertEqual(WAIST_WID, 1)

    def test_waist_len(self):
        self.assertEqual(WAIST_LEN, 1.6)

    def test_pelvis_wid(self):
        self.assertEqual(PELVIS_WID, 1)

    def test_pelvis_len(self):
        self.assertEqual(PELVIS_LEN, 1)

    def test_thigh_wid(self):
        self.assertEqual(THIGH_WID, 0.8)

    def test_thigh_len(self):
        self.assertEqual(THIGH_LEN, 5)

    def test_thigh_size(self):
        self.assertEqual(THIGH_SIZE, 50)

    def test_calf_wid(self):
        self.assertEqual(CALF_WID, 0.5)

    def test_calf_len(self):
        self.assertEqual(CALF_LEN, 4)

    def test_calf_size(self):
        self.assertEqual(CALF_SIZE, 40)

    def test_foot_wid(self):
        self.assertEqual(FOOT_WID, 1)

    def test_foot_len(self):
        self.assertEqual(FOOT_LEN, 0.5)

    def test_max_extended(self):
        self.assertEqual(MAX_EXTENDED, 300)

    def test_max_retracted(self):
        self.assertEqual(MAX_RETRACTED, 240)

    def test_upperarm_wid(self):
        self.assertEqual(UPPERARM_WID, 0.6)

    def test_upperarm_len(self):
        self.assertEqual(UPPERARM_LEN, 4)

    def test_upperarm_size(self):
        self.assertEqual(UPPERARM_SIZE, 40)

    def test_forearm_wid(self):
        self.assertEqual(FOREARM_WID, 0.4)

    def test_forearm_len(self):
        self.assertEqual(FOREARM_LEN, 3)

    def test_forearm_size(self):
        self.assertEqual(FOREARM_SIZE, 30)

    def test_hand_wid(self):
        self.assertEqual(HAND_WID, 0.5)

    def test_hand_len(self):
        self.assertEqual(HAND_LEN, 0.5)

    def test_face_heading(self):
        self.assertEqual(FACE_HEADING, 270)

    def test_face_pos_x(self):
        self.assertEqual(FACE_POS_X, 6)

    def test_face_pos_y(self):
        self.assertEqual(FACE_POS_Y, 87)

    def test_cranium_heading(self):
        self.assertEqual(CRANIUM_HEADING, 270)

    def test_cranium_pos_x(self):
        self.assertEqual(CRANIUM_POS_X, 2)

    def test_cranium_pos_y(self):
        self.assertEqual(CRANIUM_POS_Y, 92)

    def test_shoulders_heading(self):
        self.assertEqual(SHOULDERS_HEADING, 90)

    def test_shoulders_pos_x(self):
        self.assertEqual(SHOULDERS_POS_X, -2)

    def test_shoulders_pos_y(self):
        self.assertEqual(SHOULDERS_POS_Y, 76)

    def test_chest_heading(self):
        self.assertEqual(CHEST_HEADING, 0)

    def test_chest_pos_x(self):
        self.assertEqual(CHEST_POS_X, 0)

    def test_chest_pos_y(self):
        self.assertEqual(CHEST_POS_Y, 60)

    def test_waist_heading(self):
        self.assertEqual(WAIST_HEADING, 270)

    def test_waist_pos_x(self):
        self.assertEqual(WAIST_POS_X, 0)

    def test_waist_pos_y(self):
        self.assertEqual(WAIST_POS_Y, 40)

    def test_pelvis_heading(self):
        self.assertEqual(PELVIS_HEADING, 0)

    def test_pelvis_pos_x(self):
        self.assertEqual(PELVIS_POS_X, -1)

    def test_pelvis_pos_y(self):
        self.assertEqual(PELVIS_POS_Y, 10)

    def test_thigh_heading(self):
        self.assertEqual(THIGH_HEADING, 270)

    def test_thigh_pos_x(self):
        self.assertEqual(THIGH_POS_X, 0)

    def test_thigh_pos_y(self):
        self.assertEqual(THIGH_POS_Y, 0)

    def test_calf_heading(self):
        self.assertEqual(CALF_HEADING, 270)

    def test_calf_pos_x(self):
        self.assertEqual(CALF_POS_X, -2)

    def test_calf_pos_y(self):
        self.assertEqual(CALF_POS_Y, -50)

    def test_foot_heading(self):
        self.assertEqual(FOOT_HEADING, 270)

    def test_foot_pos_x(self):
        self.assertEqual(FOOT_POS_X, 5)

    def test_foot_pos_y(self):
        self.assertEqual(FOOT_POS_Y, -94)

    def test_upperarm_heading(self):
        self.assertEqual(UPPERARM_HEADING, 270)

    def test_upperarm_pos_x(self):
        self.assertEqual(UPPERARM_POS_X, -2)

    def test_upperarm_pos_y(self):
        self.assertEqual(UPPERARM_POS_Y, 65)

    def test_forearm_heading(self):
        self.assertEqual(FOREARM_HEADING, 270)

    def test_forearm_pos_x(self):
        self.assertEqual(FOREARM_POS_X, 0)

    def test_forearm_pos_y(self):
        self.assertEqual(FOREARM_POS_Y, 26)

    def test_hand_heading(self):
        self.assertEqual(HAND_HEADING, 0)

    def test_hand_pos_x(self):
        self.assertEqual(HAND_POS_X, 2)

    def test_hand_pos_y(self):
        self.assertEqual(HAND_POS_Y, -4)

    def test_carry_upperarm_heading(self):
        self.assertEqual(CARRY_UPPERARM_HEADING, 270)

    def test_carry_left_forearm_heading(self):
        self.assertEqual(CARRY_LEFT_FOREARM_HEADING, 180)

    def test_carry_left_forearm_pos_x(self):
        self.assertEqual(CARRY_LEFT_FOREARM_POS_X, 0)

    def test_carry_left_forearm_pos_y(self):
        self.assertEqual(CARRY_LEFT_FOREARM_POS_Y, -40)

    def test_carry_left_hand_pos_x(self):
        self.assertEqual(CARRY_LEFT_HAND_POS_X, 30)

    def test_carry_left_hand_pos_y(self):
        self.assertEqual(CARRY_LEFT_HAND_POS_Y, -38)

    def test_carry_right_forearm_heading(self):
        self.assertEqual(CARRY_RIGHT_FOREARM_HEADING, 0)

    def test_carry_right_forearm_pos_x(self):
        self.assertEqual(CARRY_RIGHT_FOREARM_POS_X, 0)

    def test_carry_right_forearm_pos_y(self):
        self.assertEqual(CARRY_RIGHT_FOREARM_POS_Y, -40)

    def test_carry_right_hand_pos_x(self):
        self.assertEqual(CARRY_RIGHT_HAND_POS_X, 30)

    def test_carry_right_hand_pos_y(self):
        self.assertEqual(CARRY_RIGHT_HAND_POS_Y, -38)

    def test_background_empty_mid_name(self):
        self.assertEqual(BACKGROUND_EMPTY_MID_NAME, "background_empty_mid")

    def test_background_empty_left_name(self):
        self.assertEqual(BACKGROUND_EMPTY_LEFT_NAME, "background_empty_left")

    def test_background_empty_right_name(self):
        self.assertEqual(BACKGROUND_EMPTY_RIGHT_NAME, "background_empty_right")

    def test_background_light_name(self):
        self.assertEqual(BACKGROUND_LIGHT_NAME, "background_light")

    def test_light_lift_name(self):
        self.assertEqual(LIGHT_LIFT_NAME, "light_lift")

    def test_background_regular_name(self):
        self.assertEqual(BACKGROUND_REGULAR_NAME, "background_regular")

    def test_regular_lift_name(self):
        self.assertEqual(REGULAR_LIFT_NAME, "regular_lift")

    def test_background_heavy_name(self):
        self.assertEqual(BACKGROUND_HEAVY_NAME, "background_heavy")

    def test_heavy_lift_name(self):
        self.assertEqual(HEAVY_LIFT_NAME, "heavy_lift")

    def test_background_conveyor_name(self):
        self.assertEqual(BACKGROUND_CONVEYOR_NAME, "background_conveyor")

    def test_conveyor_lift_name(self):
        self.assertEqual(CONVEYOR_LIFT_NAME, "conveyor_lift")

    def test_conveyor_belt_name(self):
        self.assertEqual(CONVEYOR_BELT_NAME, "conveyor_belt")

    def test_conveyor_drive_name(self):
        self.assertEqual(CONVEYOR_DRIVE_NAME, "conveyor_drive")

    def test_conveyor_tail_name(self):
        self.assertEqual(CONVEYOR_TAIL_NAME, "conveyor_tail")

    def test_light_lift_speed(self):
        self.assertEqual(LIGHT_LIFT_SPEED, 1)

    def test_regular_lift_speed(self):
        self.assertEqual(REGULAR_LIFT_SPEED, 1)

    def test_heavy_lift_speed(self):
        self.assertEqual(HEAVY_LIFT_SPEED, 1)

    def test_conveyor_lift_speed(self):
        self.assertEqual(CONVEYOR_LIFT_SPEED, 1)

    def test_background_empty_mid_wid(self):
        self.assertEqual(BACKGROUND_EMPTY_MID_WID, 19)

    def test_background_empty_mid_len(self):
        self.assertEqual(BACKGROUND_EMPTY_MID_LEN, 40)

    def test_background_empty_left_wid(self):
        self.assertEqual(BACKGROUND_EMPTY_LEFT_WID, 19)

    def test_background_empty_left_len(self):
        self.assertEqual(BACKGROUND_EMPTY_LEFT_LEN, 40)

    def test_background_empty_right_wid(self):
        self.assertEqual(BACKGROUND_EMPTY_RIGHT_WID, 19)

    def test_background_empty_right_len(self):
        self.assertEqual(BACKGROUND_EMPTY_RIGHT_LEN, 40)

    def test_background_light_wid(self):
        self.assertEqual(BACKGROUND_LIGHT_WID, 25)

    def test_background_light_len(self):
        self.assertEqual(BACKGROUND_LIGHT_LEN, 40)

    def test_background_regular_wid(self):
        self.assertEqual(BACKGROUND_REGULAR_WID, 25)

    def test_background_regular_len(self):
        self.assertEqual(BACKGROUND_REGULAR_LEN, 40)

    def test_background_heavy_wid(self):
        self.assertEqual(BACKGROUND_HEAVY_WID, 25)

    def test_background_heavy_len(self):
        self.assertEqual(BACKGROUND_HEAVY_LEN, 40)

    def test_background_conveyor_wid(self):
        self.assertEqual(BACKGROUND_CONVEYOR_WID, 25)

    def test_background_conveyor_len(self):
        self.assertEqual(BACKGROUND_CONVEYOR_LEN, 40)

    def test_light_lift_wid(self):
        self.assertEqual(LIGHT_LIFT_WID, 0.2)

    def test_light_lift_len(self):
        self.assertEqual(LIGHT_LIFT_LEN, 8)

    def test_regular_lift_wid(self):
        self.assertEqual(REGULAR_LIFT_WID, 0.2)

    def test_regular_lift_len(self):
        self.assertEqual(REGULAR_LIFT_LEN, 8)

    def test_heavy_lift_wid(self):
        self.assertEqual(HEAVY_LIFT_WID, 0.2)

    def test_heavy_lift_len(self):
        self.assertEqual(HEAVY_LIFT_LEN, 8)

    def test_conveyor_lift_wid(self):
        self.assertEqual(CONVEYOR_LIFT_WID, 0.2)

    def test_conveyor_lift_len(self):
        self.assertEqual(CONVEYOR_LIFT_LEN, 8)

    def test_conveyor_belt_wid(self):
        self.assertEqual(CONVEYOR_BELT_WID, 2)

    def test_conveyor_belt_len(self):
        self.assertEqual(CONVEYOR_BELT_LEN, 20)

    def test_conveyor_drive_wid(self):
        self.assertEqual(CONVEYOR_DRIVE_WID, 2)

    def test_conveyor_drive_len(self):
        self.assertEqual(CONVEYOR_DRIVE_LEN, 2)

    def test_conveyor_tail_wid(self):
        self.assertEqual(CONVEYOR_TAIL_WID, 2)

    def test_conveyor_tail_len(self):
        self.assertEqual(CONVEYOR_TAIL_LEN, 2)

    def test_background_empty_mid_heading(self):
        self.assertEqual(BACKGROUND_EMPTY_MID_HEADING, 0)

    def test_background_empty_mid_pos_x(self):
        self.assertEqual(BACKGROUND_EMPTY_MID_POS_X, 0)

    def test_background_empty_mid_pos_y(self):
        self.assertEqual(BACKGROUND_EMPTY_MID_POS_Y, 210)

    def test_background_empty_left_heading(self):
        self.assertEqual(BACKGROUND_EMPTY_LEFT_HEADING, 0)

    def test_background_empty_left_pos_x(self):
        self.assertEqual(BACKGROUND_EMPTY_LEFT_POS_X, -3200)

    def test_background_empty_left_pos_y(self):
        self.assertEqual(BACKGROUND_EMPTY_LEFT_POS_Y, 210)

    def test_background_empty_right_heading(self):
        self.assertEqual(BACKGROUND_EMPTY_RIGHT_HEADING, 0)

    def test_background_empty_right_pos_x(self):
        self.assertEqual(BACKGROUND_EMPTY_RIGHT_POS_X, 1600)

    def test_background_empty_right_pos_y(self):
        self.assertEqual(BACKGROUND_EMPTY_RIGHT_POS_Y, 210)

    def test_background_light_heading(self):
        self.assertEqual(BACKGROUND_LIGHT_HEADING, 0)

    def test_background_light_pos_x(self):
        self.assertEqual(BACKGROUND_LIGHT_POS_X, -1600)

    def test_background_light_pos_y(self):
        self.assertEqual(BACKGROUND_LIGHT_POS_Y, 150)

    def test_background_regular_heading(self):
        self.assertEqual(BACKGROUND_REGULAR_HEADING, 0)

    def test_background_regular_pos_x(self):
        self.assertEqual(BACKGROUND_REGULAR_POS_X, -800)

    def test_background_regular_pos_y(self):
        self.assertEqual(BACKGROUND_REGULAR_POS_Y, 150)

    def test_background_heavy_heading(self):
        self.assertEqual(BACKGROUND_HEAVY_HEADING, 0)

    def test_background_heavy_pos_x(self):
        self.assertEqual(BACKGROUND_HEAVY_POS_X, -2400)

    def test_background_heavy_pos_y(self):
        self.assertEqual(BACKGROUND_HEAVY_POS_Y, 150)

    def test_background_conveyor_heading(self):
        self.assertEqual(BACKGROUND_CONVEYOR_HEADING, 0)

    def test_background_conveyor_pos_x(self):
        self.assertEqual(BACKGROUND_CONVEYOR_POS_X, 800)

    def test_background_conveyor_pos_y(self):
        self.assertEqual(BACKGROUND_CONVEYOR_POS_Y, 150)

    def test_light_lift_heading(self):
        self.assertEqual(LIGHT_LIFT_HEADING, 0)

    def test_light_lift_pos_x(self):
        self.assertEqual(LIGHT_LIFT_POS_X, 0)

    def test_light_lift_pos_y(self):
        self.assertEqual(LIGHT_LIFT_POS_Y, 18)

    def test_light_lift_min_y(self):
        self.assertEqual(LIGHT_LIFT_MIN_Y, 18)

    def test_light_lift_max_y(self):
        self.assertEqual(LIGHT_LIFT_MAX_Y, 402)

    def test_regular_lift_heading(self):
        self.assertEqual(REGULAR_LIFT_HEADING, 0)

    def test_regular_lift_pos_x(self):
        self.assertEqual(REGULAR_LIFT_POS_X, 0)

    def test_regular_lift_pos_y(self):
        self.assertEqual(REGULAR_LIFT_POS_Y, 18)

    def test_regular_lift_min_y(self):
        self.assertEqual(REGULAR_LIFT_MIN_Y, 18)

    def test_regular_lift_max_y(self):
        self.assertEqual(REGULAR_LIFT_MAX_Y, 402)

    def test_heavy_lift_heading(self):
        self.assertEqual(HEAVY_LIFT_HEADING, 0)

    def test_heavy_lift_pos_x(self):
        self.assertEqual(HEAVY_LIFT_POS_X, 0)

    def test_heavy_lift_pos_y(self):
        self.assertEqual(HEAVY_LIFT_POS_Y, 18)

    def test_heavy_lift_min_y(self):
        self.assertEqual(HEAVY_LIFT_MIN_Y, 18)

    def test_heavy_lift_max_y(self):
        self.assertEqual(HEAVY_LIFT_MAX_Y, 402)

    def test_conveyor_lift_heading(self):
        self.assertEqual(CONVEYOR_LIFT_HEADING, 0)

    def test_conveyor_lift_pos_x(self):
        self.assertEqual(CONVEYOR_LIFT_POS_X, 305)

    def test_conveyor_lift_pos_y(self):
        self.assertEqual(CONVEYOR_LIFT_POS_Y, -98)

    def test_conveyor_lift_min_y(self):
        self.assertEqual(CONVEYOR_LIFT_MIN_Y, -98)

    def test_conveyor_lift_max_y(self):
        self.assertEqual(CONVEYOR_LIFT_MAX_Y, 18)

    def test_conveyor_belt_heading(self):
        self.assertEqual(CONVEYOR_BELT_HEADING, 0)

    def test_conveyor_belt_pos_x(self):
        self.assertEqual(CONVEYOR_BELT_POS_X, 0)

    def test_conveyor_belt_pos_y(self):
        self.assertEqual(CONVEYOR_BELT_POS_Y, 0)

    def test_conveyor_drive_heading(self):
        self.assertEqual(CONVEYOR_DRIVE_HEADING, 0)

    def test_conveyor_drive_pos_x(self):
        self.assertEqual(CONVEYOR_DRIVE_POS_X, -200)

    def test_conveyor_drive_pos_y(self):
        self.assertEqual(CONVEYOR_DRIVE_POS_Y, 0)

    def test_conveyor_tail_heading(self):
        self.assertEqual(CONVEYOR_TAIL_HEADING, 0)

    def test_conveyor_tail_pos_x(self):
        self.assertEqual(CONVEYOR_TAIL_POS_X, 200)

    def test_conveyor_tail_pos_y(self):
        self.assertEqual(CONVEYOR_TAIL_POS_Y, 0)

    def test_leftmost_term(self):
        self.assertEqual(LEFTMOST_TERM, -1600)

    def test_rightmost_term(self):
        self.assertEqual(RIGHTMOST_TERM, 3200)

    def test_factory_left_end(self):
        self.assertEqual(FACTORY_LEFT_END, 400)

    def test_factory_right_end(self):
        self.assertEqual(FACTORY_RIGHT_END, -400)

    def test_name_light_box(self):
        self.assertEqual(NAME_LIGHT_BOX, "light_box")

    def test_name_regular_box(self):
        self.assertEqual(NAME_REGULAR_BOX, "regular_box")

    def test_name_heavy_box(self):
        self.assertEqual(NAME_HEAVY_BOX, "heavy_box")

    def test_box_left_speed(self):
        self.assertEqual(BOX_LEFT_SPEED, -1)

    def test_box_light_shapesize(self):
        self.assertEqual(BOX_LIGHT_SHAPESIZE, (1, 1, 1))

    def test_box_light_wid(self):
        self.assertEqual(BOX_LIGHT_WID, 1)

    def test_box_light_len(self):
        self.assertEqual(BOX_LIGHT_LEN, 1)

    def test_box_regular_shapesize(self):
        self.assertEqual(BOX_REGULAR_SHAPESIZE, (2, 2, 1))

    def test_box_regular_wid(self):
        self.assertEqual(BOX_REGULAR_WID, 2)

    def test_box_regular_len(self):
        self.assertEqual(BOX_REGULAR_LEN, 2)

    def test_box_heavy_shapesize(self):
        self.assertEqual(BOX_HEAVY_SHAPESIZE, (3, 3, 1))

    def test_box_heavy_wid(self):
        self.assertEqual(BOX_HEAVY_WID, 3)

    def test_box_heavy_len(self):
        self.assertEqual(BOX_HEAVY_LEN, 3)

    def test_light_box_heading(self):
        self.assertEqual(LIGHT_BOX_HEADING, 0)

    def test_light_box_pos_x(self):
        self.assertEqual(LIGHT_BOX_POS_X, 30)

    def test_light_box_pos_y(self):
        self.assertEqual(LIGHT_BOX_POS_Y, 43)

    def test_regular_box_heading(self):
        self.assertEqual(REGULAR_BOX_HEADING, 0)

    def test_regular_box_pos_x(self):
        self.assertEqual(REGULAR_BOX_POS_X, 35)

    def test_regular_box_pos_y(self):
        self.assertEqual(REGULAR_BOX_POS_Y, 53)

    def test_heavy_box_heading(self):
        self.assertEqual(HEAVY_BOX_HEADING, 0)

    def test_heavy_box_pos_x(self):
        self.assertEqual(HEAVY_BOX_POS_X, 45)

    def test_heavy_box_pos_y(self):
        self.assertEqual(HEAVY_BOX_POS_Y, 63)

    def test_transport_x(self):
        self.assertEqual(TRANSPORT_X, 0)

    def test_light_transport_y(self):
        self.assertEqual(LIGHT_TRANSPORT_Y, 13)

    def test_regular_transport_y(self):
        self.assertEqual(REGULAR_TRANSPORT_Y, 23)

    def test_heavy_transport_y(self):
        self.assertEqual(HEAVY_TRANSPORT_Y, 33)

    def test_box_pickup_pos_x(self):
        self.assertEqual(BOX_PICKUP_POS_X, -1000)

    def test_box_above_screen_pos_x(self):
        self.assertEqual(BOX_ABOVE_SCREEN_POS_X, 0)

    def test_box_above_screen_pos_y(self):
        self.assertEqual(BOX_ABOVE_SCREEN_POS_Y, 500)

    def test_adjust_y(self):
        self.assertEqual(ADJUST_Y, 0)

    def test_box_index(self):
        self.assertEqual(BOX_INDEX, -1)

    def test_surface_wid(self):
        self.assertEqual(SURFACE_WID, 0.05)

    def test_surface_len(self):
        self.assertEqual(SURFACE_LEN, 40)

    def test_surface_heading(self):
        self.assertEqual(SURFACE_HEADING, 0)

    def test_surface_pos_x(self):
        self.assertEqual(SURFACE_POS_X, 0)

    def test_surface_pos_y(self):
        self.assertEqual(SURFACE_POS_Y, -100)

    def test_info_pos_x(self):
        self.assertEqual(INFO_POS_X, 0)

    def test_info_pos_y(self):
        self.assertEqual(INFO_POS_Y, -380)

    def test_info_align(self):
        self.assertEqual(INFO_ALIGN, "center")

    def test_info_text(self):
        self.assertEqual(INFO_TEXT, "Use Left and Right arrow keys to control \
humanoid")
