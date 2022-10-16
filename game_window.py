import curses
import keyboard
import pygame
from curses import panel


class GameWindow:
    def __init__(self, height, width, begin_y, begin_x, fps):
        self.window = curses.newwin(height, width, begin_y, begin_x)
        self.height = height
        self.width = width
        self.window.keypad(True)
        pygame.init()
        self.fps = fps
        self.fpsClock = pygame.time.Clock()

    def translate_event(self):
        if keyboard.is_pressed("up arrow"):
            return 'KEY_LEFT'
        if keyboard.is_pressed("down arrow"):
            return 'KEY_RIGHT'
        if keyboard.is_pressed("left arrow"):
            return 'KEY_UP'
        if keyboard.is_pressed("right arrow"):
            return 'KEY_DOWN'
        if keyboard.is_pressed("esc"):
            return 'QUIT'

    def draw_segment(self, y, x):
        if x == self.width - 1 and y == self.height - 1:
            pass
        else:
            self.window.addstr(y, x, "*")

    def draw_fruit(self, y, x):
        if x == self.width - 1 and y == self.height - 1:
            pass
        else:
            self.window.addstr(y, x, "ó")

    def clear(self):
        self.window.clear()

    def refresh(self):
        self.window.refresh()

    def fpsTick(self):
        self.fpsClock.tick(self.fps)
