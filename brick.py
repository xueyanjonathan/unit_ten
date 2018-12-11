import pygame


class Brick:

    def __init__(self, main_surface, width, height, color):
        """
        Construct a class which can draw one brick.
        :param main_surface: The brick will be drawn in the main window.
        :param width: Brick width
        :param height: Brick height
        :param color: Brick color
        """
        self.main_surface = main_surface
        self.width = width
        self.height = height
        self.color = color

    def draw_brick(self, x, y):
        """
        The class executing the command drawing a brick.
        :param x: x coordinate of the top left of the brick.
        :param y: y coordinate of the top left of the brick.
        :return: Nothing
        """
        pygame.draw.rect(self.main_surface, self.color, (x, y, self.width, self.height), 0)
        # Show the brick
        pygame.display.update()
