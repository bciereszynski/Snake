import pygame
from pygame.locals import *
import os
from menu import Menu


class Screen:
    def __init__(self):

        self.height = 20
        self.width = 15
        self.cellSize = 41

        pygame.init()

        self.DISPLAYSURF = pygame.display.set_mode(
            (self.cellSize * self.height, self.cellSize * self.width))
        pygame.display.set_caption('Snake')

        m = Menu(self.DISPLAYSURF)


if __name__ == "__main__":
    gameMenu = Screen()
    os._exit(os.X_OK)
