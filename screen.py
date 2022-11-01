import pygame
from pygame.locals import *
import os
from game_window import GameWindow
#from menu import Menu
from logic.game import Game
from logic.settings import Settings

# game terminal with static overlay and dynamic gamewindow
# screen != menu, to enable submenus


class Screen:
    def __init__(self):
        self.settings = Settings()

    '''
    Methods used by menu buttons
    '''

    def init_game(self):
        window = GameWindow(20, 15,
                            self.settings.getDifficulty()[1])
        game = Game(window, self.settings)
        game.play()


if __name__ == "__main__":
    gameMenu = Screen()
    gameMenu.init_game()
    os._exit(os.X_OK)
