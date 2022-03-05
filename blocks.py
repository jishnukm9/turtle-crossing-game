from turtle import Turtle
import random


COLORS=['red','green','black','violet','yellow','orange']
BLOCKS_MOVE_DISTANCE=5

class Blocks():
    def __init__(self):
        self.all_blocks=[]
        self.speed_of_blocks=BLOCKS_MOVE_DISTANCE

    def create_block(self):
        creating_block_duration=random.randint(1,6)
        if creating_block_duration==1:
            block=Turtle('square')
            block.penup()
            block.shapesize(stretch_wid=1,stretch_len=2)
            block.color(random.choice(COLORS))
            y_position=random.randint(-250,250)
            block.goto(300,y_position)
            self.all_blocks.append(block)


    def move_blocks(self):
        for block in self.all_blocks:
            block.backward(self.speed_of_blocks)
    def increase_speed(self):
        self.speed_of_blocks+=5