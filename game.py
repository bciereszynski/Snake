
import pygame
import keyboard

from snake import Snake


class Game:
    def __init__(self, window):
        self.fruit_count = 2
        self.window = window
        self.snake = Snake(window.height, window.width, self.fruit_count)

        pygame.init()
        self.fps = 10
        self.fpsClock = pygame.time.Clock()

    def draw_food(self, snake):
        for fruit in snake.food_provider.food:
            self.window.draw_fruit(fruit[0], fruit[1])

    def draw_snake(self, snake):
        for segment in snake.segments:
            self.window.draw_segment(segment[0], segment[1])

    # curses have CURSED orientation

    def translate_event(self):
        if keyboard.is_pressed("up arrow"):
            return 'KEY_LEFT'
        if keyboard.is_pressed("down arrow"):
            return 'KEY_RIGHT'
        if keyboard.is_pressed("left arrow"):
            return 'KEY_UP'
        if keyboard.is_pressed("right arrow"):
            return 'KEY_DOWN'

    def play(self):
        while True:
            if self.snake.move() == 1:
                self.window.end(1)
                break
            self.window.clear()
            self.draw_snake(self.snake)
            self.draw_food(self.snake)
            self.window.refresh()
            self.snake.react(self.translate_event())
            self.fpsClock.tick(self.fps)

        self.window.clear()
