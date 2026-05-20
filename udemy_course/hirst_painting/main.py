# import colorgram
# colors = colorgram.extract('image.jpg', 20)
# print(colors)
# print("------------------")
# print(colors[0])
# print("------------------")
# print(colors[0].rgb)
# print("------------------")
# print(colors[0].hsl)

# rgb_colors = []
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

# print(rgb_colors)

# Requiremets:

# 10 x 10 dots
# dots are 20 in size
# dots are 50 in distance

import random
from turtle import Turtle, Screen, colormode
import time

color_list = [
    (228, 0, 87),
    (126, 87, 60),
    (48, 170, 224),
    (47, 172, 102),
    (197, 189, 17),
    (235, 220, 0),
    (191, 229, 249),
    (210, 202, 145),
    (235, 110, 145),
    (102, 192, 187),
    (227, 25, 114),
    (233, 78, 28),
    (1, 72, 148),
    (218, 176, 69),
    (223, 45, 122),
    (14, 79, 146),
    (244, 159, 193),
]
ROWS = 10
DOTS_PER_ROW = 10
DISTANCE = 50
DOT_SIZE = 20

turtle = Turtle()
turtle.speed(6)
turtle.pensize(2)
turtle.setx(0)
turtle.hideturtle()
first_position = turtle.position()[0]
colormode(255)


def get_random_color():
    i = random.randint(0, len(color_list) - 1)
    return (color_list[i][0], color_list[i][1], color_list[i][2])


def draw_dot_row(length):
    for x in range(length):
        r, g, b = get_random_color()
        turtle.dot(DOT_SIZE, r, g, b)
        # time.sleep(0.1)
        turtle.teleport(turtle.position()[0] + DISTANCE)


for y in range(ROWS):
    draw_dot_row(DOTS_PER_ROW)

    if y == ROWS - 1:
        break

    turtle.teleport(first_position, turtle.position()[1] + DISTANCE)


screen = Screen()
screen.exitonclick()
