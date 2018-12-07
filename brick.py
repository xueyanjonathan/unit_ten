import pygame


class Brick:

    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.window_width =   window_width
        self.window_height = window_height
        self.brick_width = (float(self.window_width) / 9) + 5
        self.brick_height = brick_height
        self.color = color

    def draw_brick(self):
        pygame.draw.rect(self.main_surface, self.color, (x, y, self.brick_height, self.brick_width), 3)
        pygame.display.update()
