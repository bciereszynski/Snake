import curses
import random
import pygame
from curses import panel
from snake import Snake


class Game:
    def __init__(self, height, width, begin_y, begin_x):
        self.height = height
        self.width = width
        self.position = begin_y, begin_x

        self.window = curses.newwin(height, width, begin_y, begin_x)
        self.window.keypad(True)

        self.snake = Snake(height, width)

        pygame.init()
        self.fps = 5
        self.fpsClock = pygame.time.Clock()

    def generate_fruit(self):
        pass

    def draw_segment(self, y, x):
        if y < self.height and x < self.width:
            self.window.addstr(y, x, "*")

    def draw_food(self, y, x):
        self.window.addstr(y, x, "ó")

    def draw_snake(self, snake):
        self.window.clear()
        for segment in snake.segments:
            self.draw_segment(segment[0], segment[1])
    #curses have CURSED oreintation
    def translate_event(self, event):
        if event == curses.KEY_UP:
            return 'KEY_LEFT'
        if event == curses.KEY_DOWN:
            return 'KEY_RIGHT'
        if event == curses.KEY_LEFT:
            return 'KEY_UP'
        if event == curses.KEY_RIGHT:
            return 'KEY_DOWN'

    def test(self):
        self.window.refresh()
        while True:
            self.snake.move()
            self.draw_snake(self.snake)
            event = self.window.getch()
            self.snake.react(self.translate_event(event))

            # self.fpsClock.tick(self.fps)

        self.snake.move()
        self.window.clear()
