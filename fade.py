import turtle
import time

turtle.setup(2000,1000)
screen = turtle.Screen().screensize(1000,1000)


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


for z in range(1,5):
    for x in range(1,255):
        screen = turtle.Screen().bgcolor('#'+rgb_to_hex((0, 255, x)))

    for x in range(255,10,-1):
        screen = turtle.Screen().bgcolor('#'+rgb_to_hex((0, x, 255)))

    for x in range(1,255):
        screen = turtle.Screen().bgcolor('#'+rgb_to_hex((x, 0, 255)))

    for x in range(255,10,-1):
        screen = turtle.Screen().bgcolor('#'+rgb_to_hex((255, 0, x)))

    for x in range(1,255):
        screen = turtle.Screen().bgcolor('#'+rgb_to_hex((255, x, 0)))


    for x in range(255,10,-1):
        screen = turtle.Screen().bgcolor('#'+rgb_to_hex((x, 255, 0)))

