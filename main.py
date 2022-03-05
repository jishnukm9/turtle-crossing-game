import time
from turtle import Screen
from movingturtle import MovingTurtle
from blocks import Blocks
from scoreboard import ScoreBoard

screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

movingturtle=MovingTurtle()
blocks=Blocks()
scoreboard=ScoreBoard()
screen.listen()

screen.onkey(movingturtle.up,'Up')


gameon=True
while gameon:
    time.sleep(0.1)
    screen.update()
    blocks.create_block()
    blocks.move_blocks()
    #detect collition
    for block in blocks.all_blocks:
        if block.distance(movingturtle)<20:
            gameon=False
            scoreboard.gameover()

    #detecting the finish line
    if movingturtle.ycor()==280:
        movingturtle.starting_position()
        blocks.increase_speed()
        scoreboard.level_increment()


screen.exitonclick()