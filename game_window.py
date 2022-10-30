import curses
import keyboard
import pygame
import time
from pygame import mixer
from curses import panel


class GameWindow:
    def __init__(self, height, width, begin_y, begin_x, fps):
        self.window = curses.newwin(height, width, begin_y, begin_x)
        self.height = height
        self.width = width
        self.window.keypad(True)
        self.segment = "@"
        self.fruit = "Ó"

        pygame.init()
        self.fps = fps
        self.fpsClock = pygame.time.Clock()

        mixer.init()
        mixer.music.load("sound.mp3")
        mixer.music.set_volume(0.1)

        curses.init_pair(5, curses.COLOR_RED, 0)
        curses.init_pair(6, curses.COLOR_GREEN, 0)

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

    def sound(self):
        mixer.music.play()

    def draw_segment(self, y, x):
        if x == self.width - 1 and y == self.height - 1:
            pass
        else:
            self.window.addstr(y, x, self.segment, curses.color_pair(6))

    def draw_fruit(self, y, x):
        if x == self.width - 1 and y == self.height - 1:
            pass
        else:
            self.window.addstr(y, x, self.fruit, curses.color_pair(5))

    def clear(self):
        self.window.clear()

    def refresh(self):
        self.window.refresh()

    def gameover(self, points):
        msgTop = "  GAME OVER!  "
        msgBottom = "  Points: " + str(points) + "  "
        self.window.addstr(self.height // 2, self.width //
                           2 - len(msgTop) // 2, msgTop)
        self.window.addstr(self.height // 2 + 1, self.width //
                           2 - len(msgBottom) // 2, msgBottom)
        self.window.refresh()
        time.sleep(2.5)

        self.window.getch()

    def fpsTick(self):
        self.fpsClock.tick(self.fps)
