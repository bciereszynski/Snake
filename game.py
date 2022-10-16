
from snake import Snake


class Game:
    def __init__(self, window):
        self.fruit_count = 2
        self.points = 0
        self.window = window
        self.snake = Snake(window.height, window.width, self.fruit_count)

    def draw_food(self, snake):
        for fruit in snake.food_provider.food:
            self.window.draw_fruit(fruit[0], fruit[1])

    def draw_snake(self, snake):
        for segment in snake.segments:
            self.window.draw_segment(segment[0], segment[1])

    # curses have CURSED orientation

    def play(self):
        while True:
            result = self.snake.move()
            if result ==-1:
                break
            elif result == 1:
                self.points = self.points + 1
            self.window.clear()
            self.draw_snake(self.snake)
            self.draw_food(self.snake)
            self.window.refresh()
            if self.snake.react(self.window.translate_event()) == 1:
                break
            self.window.fpsTick()

        self.window.clear()
