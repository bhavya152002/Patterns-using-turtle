import turtle
t = turtle.Turtle()
l = ["red", "pink", "blue", "cyan", "green", "yellow"]
for i in range (200):
    t.color(l[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)

turtle.done()    