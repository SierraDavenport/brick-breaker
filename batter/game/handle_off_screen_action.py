from game.action import Action
from game import constants
from game.point import Point
from game.audio_service import AudioService
from game.actor import Actor

audio_service = AudioService()

class Handle_Off_Screen_Action(Action):
    
    def execute(self, cast):
        ball = cast["balls"][0]
        paddle = cast["paddle"][0]
        
        if ball.get_position().get_x() <= 1:
                audio_service.play_sound(constants.SOUND_BOUNCE)
                ball.set_velocity(Point(ball.get_velocity().get_x() * -1, ball.get_velocity().get_y()))
        if ball.get_position().get_x() >= 776:
                audio_service.play_sound(constants.SOUND_BOUNCE)
                ball.set_velocity(Point(ball.get_velocity().get_x() * -1, ball.get_velocity().get_y()))
        if ball.get_position().get_y() <= 0:
                audio_service.play_sound(constants.SOUND_BOUNCE)
                ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))
        if ball.get_position().get_y() >= 576:
                audio_service.play_sound(constants.SOUND_BOUNCE)
                ball.set_position(Point(380, 500))
                paddle.set_position(Point(345, 530))




