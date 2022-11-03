import pygame
import sys
from pygame.locals import *

from game_window import GameWindow
from logic.game import Game
from logic.settings import Settings


class Menu(object):
    def __init__(self, surface):
        self.settings = Settings()
        self.cellSize = 41
        self.click = False
        self.surface = surface
        self.font = pygame.font.SysFont(None, 20)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        self.menuClock = pygame.time.Clock()
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        while True:

            surface.fill(BLACK)

            mx, my = pygame.mouse.get_pos()

            if button_1.collidepoint((mx, my)) and click:
                self.init_game()
            if button_2.collidepoint((mx, my)) and click:
                self.options()
            self.draw_text("main", WHITE, 20, 20)
            pygame.draw.rect(surface, RED, button_1)
            pygame.draw.rect(surface, RED, button_2)
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()

            self.menuClock.tick(5)

    def draw_text(self, text, color, x, y):
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.surface.blit(textobj, textrect)

    def init_game(self):
        window = GameWindow(20, 15, self.cellSize, self.surface,
                            self.settings.getDifficulty()[1])
        game = Game(window, self.settings)
        game.play()

    def options(self):
        Running = 1
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        while Running:
            self.surface.fill(BLACK)
            self.draw_text("options", WHITE, 20, 20)
            click = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Running = 0
            pygame.display.update()
            self.menuClock.tick(30)
