

class Snake:
    vectors = {
        'Up': (0, -1),
        'Down': (0, 1),
        'Left': (-1, 0),
        'Right': (1, 0),
    }

    def __init__(self, y_limit, x_limit):
        self.y_limit = y_limit
        self.x_limit = x_limit
        self.segments = [[0, 0], [1, 0], [2, 0], [2, 1]]
        self.direction = 'Right'

    def __normalize_segments(self):
        for segment in self.segments:
            if segment[0] >= self.y_limit:
                segment[0] = 0
            elif segment[0] < 0:
                segment[0] = self.y_limit - 1
            elif segment[1] >= self.x_limit:
                segment[1] = 0
            elif segment[1] < 0:
                segment[1] = self.x_limit - 1

    def move(self):
        vector = self.vectors.get(self.direction, (0, 0))
        self.segments.pop(0)
        first_segment = self.segments[-1]
        self.segments.append(
            [first_segment[0] + vector[0], first_segment[1] + vector[1]])
        self.__normalize_segments()

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
