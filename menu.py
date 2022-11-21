import pygame
import sys
from pygame.locals import *
import pygame_menu

from game_window import GameWindow
from logic.game import Game
from logic.settings import Settings


class Menu(object):

    def set_difficulty(self, value, id):
        self.settings.difficultySwitch()

    def set_sound(self, value, id):
        self.settings.soundSwitch()

    def set_map(self, value, id):
        self.settings.mapSwitch()

    def start_the_game(self):
        name, cellsX, cellsY = self.settings.getMap()
        window = GameWindow(cellsX, cellsY, self.cellSize,
                            self.settings.getDifficulty()[1])
        game = Game(window, self.settings)
        game.play()
        self.surface = pygame.display.set_mode(
            (self.sizeX,  self.sizeY))

    def __init__(self, cellSize, size):
        self.settings = Settings()
        self.cellSize = cellSize
        self.sizeX, self.sizeY = size
        self.surface = pygame.display.set_mode(
            (self.sizeX,  self.sizeY))

        submenu = pygame_menu.Menu('SETTINGS', self.sizeX, self.sizeY,
                                   theme=pygame_menu.themes.THEME_GREEN)
        submenu.add.selector(
            'Difficulty :', [('Easy', 0), ('Hard', 1)], onchange=self.set_difficulty)
        submenu.add.selector(
            'Sound :', [('ON', 1), ("OFF", 0)], onchange=self.set_sound)

        submenu.add.selector(
            'Map size :', [('Normal', 1), ("Large", 0)], onchange=self.set_map)
        submenu.add.button('Back', pygame_menu.events.BACK)

        menu = pygame_menu.Menu('MENU', self.sizeX, self.sizeY,
                                theme=pygame_menu.themes.THEME_GREEN)

        menu.add.button('Play', self.start_the_game)
        menu.add.button('Settings', submenu)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.surface)
