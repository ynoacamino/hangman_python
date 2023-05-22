"""Module for draw."""
import turtle


def new_square(tortuga, width, height):
    """Funcion creadora de cuadrados apartir de una tortuga previamente creada"""
    tortuga.forward(width)
    tortuga.right(90)
    tortuga.forward(height)
    tortuga.right(90)
    tortuga.forward(width)
    tortuga.right(90)
    tortuga.forward(height)


window = turtle.Screen()

floor = turtle.Turtle()
floor.hideturtle()
floor.speed(70)
floor.fillcolor("black")
floor.penup()
floor.goto(-200, -100)
floor.pendown()
new_square(floor, 400, 20)


turtle.done()
