import random
from random import randint
def snowflake(whatever,colours,size):
    def branch(size,branchcolour,branchnum):
        size2=size*3
        for i in range(3):
            for i in range(3):
                whatever.pensize(5)
                whatever.color('black')
                whatever.forward(size)
                whatever.backward(size)
                whatever.pensize(3)
                whatever.color(branchcolour)
                whatever.forward(size)
                whatever.backward(size)
                whatever.right(45)
            whatever.left(90)
            whatever.backward(size)
            whatever.left(45)
        whatever.right(90)
        if (branchnum < 7):
            whatever.forward(size2)

    for i in range(8):
        branchcolour=random.choice(colours)
        branch(size,branchcolour,i)
        whatever.left(45)
    whatever.pensize(1)
    
