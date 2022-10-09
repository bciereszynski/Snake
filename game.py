import curses
import random
import pygame
import keyboard
from curses import panel
from snake import Snake


class Game:
    def __init__(self, height, width, begin_y, begin_x):
        self.height = height
        self.width = width
        self.position = begin_y, begin_x

        self.window = curses.newwin(height, width, begin_y, begin_x)
        self.window.keypad(True)
        self.window.box()

        self.snake = Snake(height, width)

        pygame.init()
        self.fps = 10
        self.fpsClock = pygame.time.Clock()

    def generate_fruit(self):
        pass

    def draw_segment(self, y, x):
        if x == self.width - 1 and y == self.height - 1:
            pass
        else:
            self.window.addstr(y, x, "*")

    def draw_food(self, y, x):
        self.window.addstr(y, x, "ó")

    def draw_snake(self, snake):
        self.window.clear()
        for segment in snake.segments:
            self.draw_segment(segment[0], segment[1])
        self.window.refresh()
    # curses have CURSED oreintation

    def translate_event(self):
        if keyboard.is_pressed("up arrow"):
            return 'KEY_LEFT'
        if keyboard.is_pressed("down arrow"):
            return 'KEY_RIGHT'
        if keyboard.is_pressed("left arrow"):
            return 'KEY_UP'
        if keyboard.is_pressed("right arrow"):
            return 'KEY_DOWN'

    def test(self):
        self.window.refresh()
        while True:
            self.snake.move()
            self.draw_snake(self.snake)
            self.snake.react(self.translate_event())
            self.fpsClock.tick(self.fps)

        self.window.clear()
