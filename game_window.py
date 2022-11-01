import pygame
import time
import sys  # TODO delete
from pygame import mixer
from pygame.locals import *


class GameWindow:
    def __init__(self, size_x, size_y, fps):

        self.cellSize = 41  # have to be even
        self.height = size_x
        self.width = size_y

        self.fps = fps

        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        self.SNAKE_COLOR = WHITE
        self.FRUIT_COLOR = RED

        segmentImg = pygame.image.load('block.png')
        self.segmentImg = pygame.transform.scale(
            segmentImg, (self.cellSize, self.cellSize))

        headImg = pygame.image.load('head.png')
        self.headImg = pygame.transform.scale(
            headImg, (self.cellSize, self.cellSize))

        mixer.init()
        mixer.music.load("sound.mp3")
        mixer.music.set_volume(0.1)

        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode(
            (self.cellSize * self.height, self.cellSize * self.width))
        pygame.display.set_caption('Snake')

    def draw_background(self):
        BLACK = (0, 0, 0)
        position = (
            0, 0,
            self.height * self.cellSize, self.width * self.cellSize
        )
        pygame.draw.rect(self.DISPLAYSURF, BLACK, position)

    def draw_segment(self, x, y):
        position = (
            x * self.cellSize,
            y * self.cellSize
        )
        self.DISPLAYSURF.blit(self.segmentImg, position)

    def draw_head(self, x, y, direction):
        rotation = 0
        if direction == 'Right':
            rotation = 270
        elif direction == 'Down':
            rotation = 180
        elif direction == 'Left':
            rotation = 90
        headLocal = pygame.transform.rotate(
            self.headImg, rotation)
        position = (
            x * self.cellSize,
            y * self.cellSize
        )
        self.DISPLAYSURF.blit(headLocal, position)

    def draw_fruit(self, x, y):
        position = (
            x * self.cellSize + self.cellSize // 2,
            y * self.cellSize + self.cellSize // 2
        )
        pygame.draw.circle(self.DISPLAYSURF, self.FRUIT_COLOR,
                           position, self.cellSize // 2)

    def translate_event(self):
        for event in pygame.event.get():
            print(event.type == pygame.K_UP)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    return 'KEY_LEFT'
                if event.key == pygame.K_DOWN:
                    return 'KEY_DOWN'
                if event.key == pygame.K_RIGHT:
                    return 'KEY_RIGHT'
                if event.key == pygame.K_UP:
                    return 'KEY_UP'

            #    if keyboard.is_pressed("esc"):
            #        return 'QUIT'

    def sound(self):
        mixer.music.play()

    def clear(self):
        self.draw_background()

    def refresh(self):
        pygame.display.update()

    def gameover(self, points):
        time.sleep(2.5)

    def fpsTick(self):
        self.fpsClock.tick(self.fps)
