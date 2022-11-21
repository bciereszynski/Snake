import pygame
from pygame.locals import *
import os
from menu import Menu


class Screen:
    def __init__(self):

        self.cellsX = 20
        self.cellsY = 15
        self.cellSize = 41

        pygame.init()

        pygame.display.set_caption('Snake')

        m = Menu(self.cellSize, (self.cellSize *
                                 self.cellsX, self.cellSize * self.cellsY))


if __name__ == "__main__":
    gameMenu = Screen()
    os._exit(os.X_OK)
