class Snake:
    vectors = {
        'Up': (0, -1),
        'Down': (0, 1),
        'Left': (-1, 0),
        'Right': (1, 0),
    }

    def __init__(self):
        self.segments = [0, 5], [1, 5], [2, 5]
        self.direction = 'Right'

    def __normalize_segments(self):
        for segment in self.segments:
            if segment[0] >= GAME_CELLS_X:
                segment[0] -= GAME_CELLS_X
            elif segment[0] < 0:
                segment[0] += GAME_CELLS_X
            if segment[1] >= GAME_CELLS_Y:
                segment[1] -= GAME_CELLS_Y
            elif segment[1] < 0:
                segment[1] += GAME_CELLS_Y

    def move(self):
        vector = self.vectors.get(self.direction, (0, 0))
        self.segments.pop(0)
        first_segment = self.segments[-1]
        self.segment.append(
            first_segment[0] + vector[0], first_segment[1] + vector[1])
        self.__normalize_segments()

    def process_event(self, event):
        pass
