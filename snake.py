

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
        self.segments = [(0, 0), (1, 0), (5, 5), (15, 15)]
        self.direction = 'Right'

    def __normalize_segments(self):
        for segment in self.segments:
            if segment[0] >= self.x_limit:
                segment[0] -= self.x_limit
            elif segment[0] < 0:
                segment[0] += self.x_limit
            if segment[1] >= self.y_limit:
                segment[1] -= self.y_limit
            elif segment[1] < 0:
                segment[1] += self.y_limit

    def move(self):
        vector = self.vectors.get(self.direction, (0, 0))
        self.segments.pop(0)
        first_segment = self.segments[-1]
        self.segments.append(
            (first_segment[0] + vector[0], first_segment[1] + vector[1]))

        # self.__normalize_segments()

    def react(self, event):
        if event == 'KEY_UP':
            self.direction = 'Up'
        elif event == 'KEY_DOWN':
            self.direction = 'Down'
        elif event == 'KEY_LEFT':
            self.direction = 'Left'
        elif event == 'KEY_RIGHT':
            self.direction = 'Right'
