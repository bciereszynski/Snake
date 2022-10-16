from food_provider import FoodProvider


class Snake:
    # to moving
    vectors = {
        'Up': (0, -1),
        'Down': (0, 1),
        'Left': (-1, 0),
        'Right': (1, 0),
    }

    def __init__(self, y_limit, x_limit, fruit_count):
        self.y_limit = y_limit
        self.x_limit = x_limit

        # TODO - initial configure
        self.segments = [[0, 0], [1, 0], [2, 0], [2, 1]]
        self.direction = 'Right'
        self.has_eaten = False

        self.food_provider = FoodProvider(self, y_limit, x_limit)
        for x in range(fruit_count):
            self.food_provider.generate()

    def __normalize_segments(self):
        segment = self.segments[-1]
        if segment[0] >= self.y_limit:
            segment[0] = 0
        elif segment[0] < 0:
            segment[0] = self.y_limit - 1
        elif segment[1] >= self.x_limit:
            segment[1] = 0
        elif segment[1] < 0:
            segment[1] = self.x_limit - 1

    def try_eat(self, head, vector):
        # eat fruit
        if self.food_provider.food.count(head) != 0:
            self.food_provider.food.remove(head)
            self.has_eaten = True
            self.food_provider.generate()
            return 0
        # eat yourself
        elif self.segments.count(head) != 1:
            return 1
        else:
            return 0

    def move(self):
        # gain vector coresponding to direction
        vector = self.vectors.get(self.direction, (0, 0))
        # move last segment to front
        if self.has_eaten == False:
            self.segments.pop(0)
        else:
            self.has_eaten = False
        head = self.segments[-1]
        self.segments.append(
            [head[0] + vector[0], head[1] + vector[1]])
        self.__normalize_segments()
        # try eat - food(0) or yourself(1)
        if self.try_eat(self.segments[-1], vector) == 1:
            return 1
        return 0

    def react(self, event):
        if event == 'KEY_UP' and self.direction != 'Down':
            self.direction = 'Up'
        elif event == 'KEY_DOWN' and self.direction != 'Up':
            self.direction = 'Down'
        elif event == 'KEY_LEFT' and self.direction != 'Right':
            self.direction = 'Left'
        elif event == 'KEY_RIGHT' and self.direction != 'Left':
            self.direction = 'Right'
        else:
            pass
