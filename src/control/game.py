import utils.constants as const

class Game:
    """Controls of the game."""


    def __init__(self):
        """Initialize the game control variables."""
        self._game_on = False
        self._create_box = False
        self._created_box = False
        self._light_lift_up = False
        self._light_lift_down = False
        self._regular_lift_up = False
        self._regular_lift_down = False
        self._heavy_lift_up = False
        self._heavy_lift_down = False
        self._conveyor_lift_up = False
        self._conveyor_lift_down = False
        self._box_left = False
        self._ready_pickup = False
        self._carrying_box = False
        self._box_in_light_lift = False
        self._box_in_regular_lift = False
        self._box_in_heavy_lift = False
        self._exit_message = const.EXIT_MESSAGE
        self.box_index = const.BOX_INDEX
        self.boxes = []

    @property
    def game_on(self):
        """Get game on boolean value."""
        return self._game_on

    @game_on.setter
    def game_on(self, val):
        """Set game on boolean value."""
        self._game_on = val

    @property
    def create_box(self):
        """Get create box boolean value."""
        return self._create_box

    @create_box.setter
    def create_box(self, val):
        """Set create box boolean value."""
        self._create_box = val

    @property
    def created_box(self):
        """Get created box boolean value."""
        return self._created_box

    @created_box.setter
    def created_box(self, val):
        """Set created box boolean value."""
        self._created_box = val

    @property
    def light_lift_up(self):
        """Get light lift up boolean value."""
        return self._light_lift_up

    @light_lift_up.setter
    def light_lift_up(self, val):
        """Set light lift up boolean value."""
        self._light_lift_up = val

    @property
    def light_lift_down(self):
        """Get light lift down boolean value."""
        return self._light_lift_down

    @light_lift_down.setter
    def light_lift_down(self, val):
        """Set light lift down boolean value."""
        self._light_lift_down = val

    @property
    def regular_lift_up(self):
        """Get regular lift up boolean value."""
        return self._regular_lift_up

    @regular_lift_up.setter
    def regular_lift_up(self, val):
        """Set regular lift up boolean value."""
        self._regular_lift_up = val

    @property
    def regular_lift_down(self):
        """Get regular lift down boolean value."""
        return self._regular_lift_down

    @regular_lift_down.setter
    def regular_lift_down(self, val):
        """Set regular lift down boolean value."""
        self._regular_lift_down = val

    @property
    def heavy_lift_up(self):
        """Get heavy lift up boolean value."""
        return self._heavy_lift_up

    @heavy_lift_up.setter
    def heavy_lift_up(self, val):
        """Set heavy lift up boolean value."""
        self._heavy_lift_up = val

    @property
    def heavy_lift_down(self):
        """Get heavy lift down boolean value."""
        return self._heavy_lift_down

    @heavy_lift_down.setter
    def heavy_lift_down(self, val):
        """Set heavy lift down boolean value."""
        self._heavy_lift_down = val

    @property
    def conveyor_lift_up(self):
        """Get conveyor lift up boolean value."""
        return self._conveyor_lift_up

    @conveyor_lift_up.setter
    def conveyor_lift_up(self, val):
        """Set conveyor lift up boolean value."""
        self._conveyor_lift_up = val

    @property
    def conveyor_lift_down(self):
        """Get conveyor lift down boolean value."""
        return self._conveyor_lift_down

    @conveyor_lift_down.setter
    def conveyor_lift_down(self, val):
        """Set conveyor lift down boolean value."""
        self._conveyor_lift_down = val

    @property
    def box_left(self):
        """Get box left boolean value."""
        return self._box_left

    @box_left.setter
    def box_left(self, val):
        """Set box left boolean value."""
        self._box_left = val

    @property
    def ready_pickup(self):
        """Get box ready for pick up boolean value."""
        return self._ready_pickup

    @ready_pickup.setter
    def ready_pickup(self, val):
        """Set box ready for pick up boolean value."""
        self._ready_pickup = val

    @property
    def carrying_box(self):
        """Get carrying box boolean value."""
        return self._carrying_box

    @carrying_box.setter
    def carrying_box(self, val):
        """Set carrying box boolean value."""
        self._carrying_box = val

    @property
    def box_in_light_lift(self):
        """Get box in light lift boolean value."""
        return self._box_in_light_lift

    @box_in_light_lift.setter
    def box_in_light_lift(self, val):
        """Set box in light lift boolean value."""
        self._box_in_light_lift = val

    @property
    def box_in_regular_lift(self):
        """Get box in regular lift boolean value."""
        return self._box_in_regular_lift

    @box_in_regular_lift.setter
    def box_in_regular_lift(self, val):
        """Set box in regular lift boolean value."""
        self._box_in_regular_lift = val

    @property
    def box_in_heavy_lift(self):
        """Get box in heavy lift boolean value."""
        return self._box_in_heavy_lift

    @box_in_heavy_lift.setter
    def box_in_heavy_lift(self, val):
        """Set box in heavy lift boolean value."""
        self._box_in_heavy_lift = val

    @property
    def exit_message(self):
        """Get exit message."""
        return self._exit_message
