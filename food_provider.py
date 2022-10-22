import random


class FoodProvider:
    def __init__(self, snake, y_limit, x_limit):
        self.food = []
        self.y_limit = y_limit
        self.x_limit = x_limit
        self.snake = snake

    def generate(self):
        while True:
            i = 0
            y = random.randint(0, self.y_limit - 1)
            x = random.randint(0, self.x_limit - 1)
            if self.snake.segments.count([y, x]) == 0 and self.food.count([y,x]) == 0:
                self.food.append([y, x])
                break
            i= i + 1
            if i==1000000:
                break
