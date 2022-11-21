import pygame
import time


from pygame import mixer
from pygame.locals import *


class GameWindow:
    def __init__(self, size_x, size_y, cell_size, fps):
        self.fpsClock = pygame.time.Clock()
        self.cellSize = cell_size  # have to be even
        self.height = size_x
        self.width = size_y
        self.DISPLAYSURF = pygame.display.set_mode(
            (self.cellSize * size_x, self.cellSize * size_y))
        self.fps = fps

        self.resourcesPath = "res/"

        segmentImg = pygame.image.load(self.resourcesPath + 'block.png')
        self.segmentImg = pygame.transform.scale(
            segmentImg, (self.cellSize, self.cellSize))

        fruitImg = pygame.image.load(self.resourcesPath + 'fruit.png')
        self.fruitImg = pygame.transform.scale(
            fruitImg, (self.cellSize, self.cellSize))

        grassImg = pygame.image.load(self.resourcesPath + 'grass.jpg')
        self.grassImg = pygame.transform.scale(
            grassImg, (self.cellSize * size_x, self.cellSize * size_y))

        headImg = pygame.image.load(self.resourcesPath + 'head.png')
        self.headImg = pygame.transform.scale(
            headImg, (self.cellSize, self.cellSize))

        mixer.init()
        mixer.music.load(self.resourcesPath + "sound.mp3")
        mixer.music.set_volume(0.1)

    def draw_background(self):
        position = (
            0, 0,
            self.height * self.cellSize, self.width * self.cellSize
        )
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
            x * self.cellSize,
            y * self.cellSize
        )
        self.DISPLAYSURF.blit(self.fruitImg, position)

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
            self.height // 4 * self.cellSize, self.width // 4 * self.cellSize,
            self.height // 2 * self.cellSize, self.width // 2 * self.cellSize
        )
        s = pygame.Surface((position[2], position[3]),
                           pygame.SRCALPHA)   # per-pixel alpha
        s.fill((0, 0, 0, 128))
        self.DISPLAYSURF.blit(s, position)

        smallfont = pygame.font.SysFont('Corbel', 35)
        text = smallfont.render(
            'Points: ' + str(points), True, (255, 255, 255, 128))
        self.DISPLAYSURF.blit(
            text, (position[0] + position[2] // 2 - text.get_width() // 2, position[1] + position[3] // 2 - self.cellSize))
        text = smallfont.render("Please wait...", True, (255, 255, 255))
        self.DISPLAYSURF.blit(
            text, (position[0] + position[2] // 2 - text.get_width() // 2, position[1] + position[3] // 2 + self.cellSize))
        pygame.display.update()
        time.sleep(3)

    def fpsTick(self):
        self.fpsClock.tick(self.fps)
