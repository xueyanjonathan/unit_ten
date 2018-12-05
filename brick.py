import pygame


class Brick:

    def __init__(self, main_surface):
        self.main_surface = main_surface

    def draw_brick(self):
        pygame.draw.rect(self.main_surface, self.GREEN, (5, 5, 400, 200), 3)
        pygame.display.update()
