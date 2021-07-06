from turtle import *
from random import randint
bgcolor("black")
x=1
speed(0)
shape("classic")
while x<400:
    r = randint(0,255)
    g = randint (0,255)
    b = randint (0,255)

    colormode(255)
    pencolor(r,g,b)
    forward(5+x)
    right(90.91)
    x=x+1

exitonclick()    
