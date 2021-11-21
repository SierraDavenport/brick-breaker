
from game.action import Action
from game import constants
from game.point import Point
from game.audio_service import AudioService
from game.actor import Actor

audio_service = AudioService()

class HandleCollisionsAction(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
    def execute(self, cast):
        ball = cast["balls"][0]
        paddle = cast["paddle"][0]

        if self._physics_service.is_collision(ball, paddle):
            audio_service.play_sound(constants.SOUND_BOUNCE)
            ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))


        bricks = cast["bricks"]
        for brick in bricks:
            if self._physics_service.is_collision(ball, brick):
                audio_service.play_sound(constants.SOUND_BOUNCE)
                ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))
                bricks.remove(brick)