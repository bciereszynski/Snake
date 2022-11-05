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

    def start_the_game(self):
        window = GameWindow(20, 15, self.cellSize, self.surface,
                            self.settings.getDifficulty()[1])
        game = Game(window, self.settings)
        game.play()

    def drawBackground(self):
        self.surface.fill((255, 255, 255))

    def __init__(self, surface, cellSize):
        self.settings = Settings()
        self.cellSize = cellSize
        self.surface = surface

        submenu = pygame_menu.Menu('SUB_MENU', 400, 300,
                                   theme=pygame_menu.themes.THEME_GREEN)
        submenu.add.selector(
            'Difficulty :', [('Easy', 0), ('Hard', 1)], onchange=self.set_difficulty)
        submenu.add.selector(
            'Sound :', [('ON', 1), ("OFF", 0)], onchange=self.set_sound)
        submenu.add.button('Quit', pygame_menu.events.BACK)

        menu = pygame_menu.Menu('MAIN_MENU', 400, 300,
                                theme=pygame_menu.themes.THEME_GREEN)

        menu.add.text_input('Name :', default='John Doe')
        menu.add.button('Play', self.start_the_game)
        menu.add.button('Settings', submenu)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(surface, self.drawBackground)
