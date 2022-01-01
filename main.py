from turtle import Turtle, Screen
import random

tim = Turtle()
colours = [
    "CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
    "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"
]


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


for shape in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape)
