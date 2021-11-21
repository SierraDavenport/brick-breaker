from game.actor import Actor
from game.point import Point
from game import constants

class Ball(Actor):
    def __init__(self):
        self.set_height(constants.BALL_HEIGHT)
        self.set_width(constants.BALL_WIDTH)
        self.set_image(constants.IMAGE_BALL)
        self.set_position(Point(0,0))
        self._velocity = Point(5,5)

    def set_position(self, position):
        self._position = position
    def get_position(self):
        return self._position