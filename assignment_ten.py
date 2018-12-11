# Jonathan Lin
# 12/11/2018
# Drawing with Pygame
# Using class and methods to draw repetition of bricks

import pygame
import sys
import brick
import random
from pygame.locals import *

pygame.init()

# Assign width and height for the window
window_width = 500
window_height = 250


def get_width():
    """
    Calculate the width of a brick using the existing value window width
    :return: brick width
    """
    width = float(window_width)/9 - 5
    return width


# Assign width, height, space, and colors for the bricks
width = get_width()
height = 20
space = 5
GOLD = (255, 209, 63)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PINK = (255, 192, 203)
PURPLE = (160, 32, 240)
ORANGE = (255, 165, 0)
ROSE = (255, 228, 225)

# Get the colors into a list and randomize them. It helps randomly assigning colors to bricks later.
colors = [GOLD, BLACK, BLUE, RED, PINK, PURPLE, ORANGE, ROSE]
random.shuffle(colors)

# Create the main window and fill the background with white color.
# Name the window Brick Pyramid
mainSurface = pygame.display.set_mode((window_width, window_height), 0, 32)
mainSurface.fill(WHITE)
pygame.display.set_caption("Brick Pyramid")

# The first brick starts at the coordinate x = 0 and y = window height - height of the brick - a space
x = 0
y = window_height - height - space
bricks = 9
for rows in range(5):
    # There are five rows in total. Each row has its random color.
    color = colors.pop()
    for number in range(bricks):
        # The loop will not stop until it draws all the bricks in a row.
        pyramid = brick.Brick(mainSurface, width, height, color)
        pyramid.draw_brick(x, y)
        # After drawing a brick, move the x coordinate to the right to draw the next brick
        x = x + width + space
    # When starting a new row, the new row will have 2 less bricks than the row below.
    bricks = bricks - 2
    # To start a new row, raise the y coordinate.
    y = y - height - space
    # Reset the x coordinate to 0 after finishing a row.
    # Move the first brick at the row to the right corresponding to the number of bricks in the row.
    x = 0 + ((9 - bricks) / 2) * (space + width)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

