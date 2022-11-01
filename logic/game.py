from .snake import Snake
from .settings import Settings


class Game:
    def __init__(self, window, settings):
        self.settings = settings
        self.points = 0
        self.window = window
        self.snake = Snake(window.cellsX, window.cellsY,
                           self.settings.fruit_count)

    def draw_food(self, snake):
        for fruit in snake.food_provider.food:
            self.window.draw_fruit(fruit[0], fruit[1])

    def draw_snake(self, snake):
        for segment in snake.segments:
            self.window.draw_segment(segment[0], segment[1])

    # one snake movement
    def play(self):
        # check what happend when snake move
        result = self.snake.move()

        # react
        if result == -1:
            self.window.gameover(self.points)
            return 1

        elif result == 1:
            self.points = self.points + 1
            if self.settings.sound == 1:
                self.window.sound()

        self.window.clear()
        self.draw_snake(self.snake)
        self.draw_food(self.snake)
        self.window.refresh()

        # esc
        if self.snake.react(self.window.translate_event()) == 1:
            return 1

        self.window.fpsTick()
