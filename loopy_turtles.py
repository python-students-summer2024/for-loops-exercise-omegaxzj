"""
This file contains a few incomplete function definitions that use the turtle module.  
The turtle module is included in the default Python distribution and documented here: https://docs.python.org/3/library/turtle.html
Your task is to complete the incomplete function definitions so that they behave as indicated in the documentation.

Do not run this file directly.
Rather, call any of these functions from main.py and run that file.
"""

# import the turtle module, which is included in the regular Python distribution
import turtle


def create_turtle(stroke_color, bg_color):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(stroke_color)
    window = turtle.Screen()
    window.bgcolor(bg_color)
    return t


def pick_up_and_move_turtle(t, x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()


def print_turtle_position(t):
    print(f"Position: ({t.xcor()}, {t.ycor()}), Heading: {t.heading()}")


def draw_square(t, x, y, length, rotation_direction, fill_color):
    pick_up_and_move_turtle(t, x, y)
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(4):
        t.forward(length)
        if rotation_direction == 'right':
            t.right(90)
        else:
            t.left(90)
        print_turtle_position(t) 
    t.end_fill()


def draw_star(t, x, y, length, angle, initial_rotation_direction, fill_color):
    pick_up_and_move_turtle(t, x, y)
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(5):
        t.forward(length)
        if initial_rotation_direction == 'right':
            t.right(angle)
        else:
            t.left(angle)
        t.forward(length)
        if initial_rotation_direction == 'right':
            t.left(180 - angle)
        else:
            t.right(180 - angle) 
    t.end_fill()
    print_turtle_position(t)
