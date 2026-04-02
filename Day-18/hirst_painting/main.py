# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)  # extract 10 colors
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)


import turtle
import random
from turtle import Screen

t = turtle.Turtle()
screen = turtle.Screen()

t.speed(0)
t.penup()
t.hideturtle()

screen.colormode(255)


# Move turtle to starting position (bottom-left)
t.setheading(225)
t.forward(300)
t.setheading(0)

dots_per_row = 10
spacing = 50
colors=[(244, 242, 238), (124, 181, 211), (199, 174, 15), (247, 226, 234), (222, 232, 240), (26, 121, 168), (178, 13, 44), (237, 204, 87), (239, 148, 73), (220, 122, 162), (232, 241, 235), (25, 144, 72), (216, 80, 124), (7, 172, 211), (214, 59, 26), (66, 21, 54), (239, 77, 44), (247, 156, 189), (8, 184, 151), (161, 56, 107), (10, 30, 72), (74, 28, 23), (128, 208, 234), (13, 48, 132), (167, 193, 164), (101, 116, 184), (252, 156, 151), (167, 24, 19), (3, 88, 57), (111, 217, 215)]
for row in range(dots_per_row):
    for col in range(dots_per_row):
        t.dot(20, random.choice(colors))  # draw dot
        t.forward(spacing)

    # Move to next row
    t.backward(spacing * dots_per_row)
    t.left(90)
    t.forward(spacing)
    t.right(90)



screen.exitonclick()