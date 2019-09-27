import turtle
screen = turtle.Screen()
tr = turtle.Turtle()
tr.shape("turtle")
tr.speed(1)

tr.fillcolor("green")
tr.begin_fill()

# How to draw a square?
for _ in range(4):
    tr.forward(100)
    tr.left(90)

tr.end_fill()
tr.penup()
tr.right(90)
tr.forward(100)
tr.pendown()
tr.begin_fill()

# how to draw a triangle?
for _ in range(3):
    tr.forward(100)
    tr.left(120)

tr.end_fill()
tr.penup()
tr.right(90)
tr.forward(100)
tr.pendown()
tr.begin_fill()

# How to draw a rectangle? (width: 100, height: 50)
for _ in range(2):
    tr.forward(100)
    tr.left(90)
    tr.forward(50)
    tr.left(90)

tr.end_fill()
screen.exitonclick()
