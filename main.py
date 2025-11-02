import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("circle")
screen.setup(width=700, height=700)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

colors = ["red", "crimson", "orange", "yellow", "white", "gold", "tomato"]

print("Creating big pattern...")
print("It will take a bit time, just look after magic ✨")

pen.penup()
pen.goto(0, 0)
pen.pendown()

for i in range(500):
    pen.color(colors[i % len(colors)])
    pen.pensize(1 + (i % 6))
    pen.forward(i * 0.7)
    pen.right(89)

print("Adding big circles...")
for i in range(72):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.color(colors[i % len(colors)])
    pen.pensize(2)
    pen.setheading(i * 5)
    pen.circle(180)