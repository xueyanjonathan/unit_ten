import pygame, sys
import brick
import random
from pygame.locals import *

pygame.init()

window_width = 500
window_height = 250


def get_width():
    width = float(window_width)/9 -5
    return width


width = get_width()
height = 20
space = 5
GREEN = (0, 102, 71)
GOLD = (255, 209, 63)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PINK = (255, 192, 203)
PURPLE = (160, 32, 240)
ORANGE = (255, 165, 0)
ROSE = (255, 228, 225)

colors = [GREEN, GOLD, WHITE, BLUE, RED, BLACK, PINK, PURPLE, ORANGE, ROSE]
random.shuffle(colors)

mainSurface = pygame.display.set_mode((window_width, window_height), 0, 32)
pygame.display.set_caption("Brick Pyramid")

x = 0
y = window_height - height - space
bricks = 9
for rows in range(5):
    color = colors.pop()
    for number in range(9):
        pyramid = brick.Brick(mainSurface, width, height, color)
        pyramid.draw_brick(x, y)
        x = x + width + space
    bricks = bricks - 2
    y = y + height + space
    x = x + width + space

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
