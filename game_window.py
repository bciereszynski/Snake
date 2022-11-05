import pygame


from pygame import mixer
from pygame.locals import *


class GameWindow:
    def __init__(self, size_x, size_y, cell_size, displaysurf, fps):
        self.fpsClock = pygame.time.Clock()
        self.cellSize = cell_size  # have to be even
        self.height = size_x
        self.width = size_y
        self.DISPLAYSURF = displaysurf
        self.fps = fps

        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        self.SNAKE_COLOR = WHITE
        self.FRUIT_COLOR = RED

        segmentImg = pygame.image.load('block.png')
        self.segmentImg = pygame.transform.scale(
            segmentImg, (self.cellSize, self.cellSize))

        grassImg = pygame.image.load('grass.jpg')
        self.grassImg = pygame.transform.scale(
            grassImg, (self.cellSize * size_x, self.cellSize * size_y))

        headImg = pygame.image.load('head.png')
        self.headImg = pygame.transform.scale(
            headImg, (self.cellSize, self.cellSize))

        mixer.init()
        mixer.music.load("sound.mp3")
        mixer.music.set_volume(0.1)

    def draw_background(self):
        position = (
            0, 0,
            self.height * self.cellSize, self.width * self.cellSize
        )
        #pygame.draw.rect(self.DISPLAYSURF, BLACK, position)
        self.DISPLAYSURF.blit(self.grassImg, (0, 0))

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
                if event.key == pygame.K_ESCAPE:
                    return 'QUIT'

    def sound(self):
        mixer.music.play()

    def clear(self):
        self.draw_background()

    def refresh(self):
        pygame.display.update()

    def gameover(self, points):
        position = (
            0, 0,
            self.height * self.cellSize, self.width * self.cellSize
        )
        #pygame.draw.rect(self.DISPLAYSURF, BLACK, position)

    def fpsTick(self):
        self.fpsClock.tick(self.fps)
