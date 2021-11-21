import random
# from batter.game import handle_collisions_action
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.brick import Brick
from game.ball import Ball
from game.paddle import Paddle
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import Handle_Off_Screen_Action
from game.move_actors_action import MoveActorsAction

def main():
    x = 25
    y = 20

    # create the cast {key: tag, value: list}
    cast = {}

    cast["bricks"] = []
    # Create bricks here and add them to the list
    
    bricks = []
    num = 0
    for brick in range(0,105):
        brick = Brick()
        num += 1
        if (num % 2) == 0:
            brick.set_image(constants.IMAGE_BRICK_2)
        else:
            brick.set_image(constants.IMAGE_BRICK_1)


        
        if x > 760:
            x = 25
            y += 40

        brick.set_position(Point(x,y))

        x += 50

        bricks.append(brick)
    cast["bricks"] = bricks

    cast["balls"] = []
    # TODO: Create a ball here and add it to the list
    balls = []
    ball = Ball()
    ball.set_position(Point(380, 500))
    balls.append(ball)
    cast["balls"] = balls

    cast["paddle"] = []
    # TODO: Create a paddle here and add it to the list
    paddles = []
    paddle = Paddle()
    paddle.set_position(Point(345, 530))
    paddles.append(paddle)
    cast["paddle"] = paddles


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    handle_off_screen_action = Handle_Off_Screen_Action()
    draw_actors_action = DrawActorsAction(output_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)
    move_actors_action = MoveActorsAction()
    control_actors_action = ControlActorsAction(input_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
