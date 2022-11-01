import pygame
import sys
from pygame.locals import *

# RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SNAKE_COLOR = WHITE
FRUIT_COLOR = RED

FPS = 60

GAME_CELL_SIZE = 41  # have to be even
GAME_CELLS_X = 20
GAME_CELLS_Y = 15

segmentImg = pygame.image.load('block.png')
segmentImg = pygame.transform.scale(
    segmentImg, (GAME_CELL_SIZE, GAME_CELL_SIZE))


def draw_background(surf):
    BLACK = (0, 0, 0)
    position = (
        0, 0,
        GAME_CELLS_X * GAME_CELL_SIZE, GAME_CELLS_Y * GAME_CELL_SIZE
    )
    pygame.draw.rect(surf, BLACK, position)


def draw_segment(surf, x, y):
    position = (
        x * GAME_CELL_SIZE,
        y * GAME_CELL_SIZE
    )
    surf.blit(segmentImg, position)


def draw_food(surf, x, y):
    position = (
        x * GAME_CELL_SIZE + GAME_CELL_SIZE // 2,
        y * GAME_CELL_SIZE + GAME_CELL_SIZE // 2
    )
    pygame.draw.circle(surf, RED, position, GAME_CELL_SIZE // 2)


pygame.init()
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode(
    (GAME_CELL_SIZE * GAME_CELLS_X, GAME_CELL_SIZE * GAME_CELLS_Y))
pygame.display.set_caption('Snake')


for x in range(GAME_CELLS_X):
    for y in range(GAME_CELLS_Y):
        if (x + y) % 2 == 0:
            draw_segment(DISPLAYSURF, x, y)
        else:
            pass
