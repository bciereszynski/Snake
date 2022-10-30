import random


class FoodProvider:
    def __init__(self, snake, y_limit, x_limit):
        self.food = []
        self.y_limit = y_limit
        self.x_limit = x_limit
        self.snake = snake

    """
    Method generate random coordinates to find a free
    spot on the map and place new fruit there.
    Method has a limited number of tries.
    """

    def generate(self):
        limit = 1000000
        while True:
            i = 0
            y = random.randint(0, self.y_limit - 1)
            x = random.randint(0, self.x_limit - 1)
            if self.snake.segments.count([y, x]) == 0 and self.food.count([y, x]) == 0:
                self.food.append([y, x])
                break
            i = i + 1
            if i == limit:
                break
