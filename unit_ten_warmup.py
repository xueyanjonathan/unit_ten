import pygame, sys
import logo
from pygame.locals import *

pygame.init()

mainSurface = pygame.display.set_mode((500, 250), 0, 32)
pygame.display.set_caption("Sandy Spring Friends School")
ssfs = logo.Logo(mainSurface)
ssfs.draw_rectangles()
ssfs.draw_trellis()
ssfs.draw_words()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
