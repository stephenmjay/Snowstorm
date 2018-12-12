#!/bin/python3

import turtle
import random
from random import randint

import basicflake
import star
import snowflake


while True:
    elsa=turtle.Turtle()
    background_image="background" + str(random.randint(1,8)) + ".png"
    turtle.Screen().bgpic(background_image)
    turtle.Screen().screensize()
    turtle.Screen().setup(width = 1.0, height = 1.0)
    colours=("azure","white","lightgray","whitesmoke","lightyellow")
    elsa.speed(0)
    for q in range(200):
        elsa.penup()
        x = random.randint(-900, 900)
        y = random.randint(-400, 400)
        elsa.goto(x, y)
        elsa.pendown()
        flake=random.randint(1,3)
        if (flake == 1):
            size=randint(5,20)
            snowflake.snowflake(elsa,colours,size)
        elif (flake == 2):
            flakesize=random.randint(10,40)
            basicflake.basicflake(elsa,colours,flakesize)
        else:
            flakesize=random.randint(25,150)
            flakecolour=random.choice(colours)
            star.star(elsa,flakesize,flakecolour)
    elsa.clear()
