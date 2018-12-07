import pygame, sys
import brick
from pygame.locals import *

pygame.init()

mainSurface = pygame.display.set_mode((window)), 0, 32)
pygame.display.set_caption("Brick Pyramid")
pyramid = brick.Brick(mainSurface)
pyramid.draw_brick()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
