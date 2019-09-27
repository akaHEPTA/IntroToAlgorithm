import turtle
screen = turtle.Screen()
screen.bgcolor("#90ee90")
tr = turtle.Turtle()
tr.shape("turtle")
tr.speed(3)
tr.pensize(5)
tr.color("blue")


for _ in range(12):
    tr.penup()
    tr.forward(100)
    tr.pendown()
    tr.forward(10)
    tr.penup()
    tr.forward(20)
    tr.stamp()
    tr.back(130)
    tr.left(30)


screen.exitonclick()
