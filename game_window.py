import curses
from curses import panel


class GameWindow:
    def __init__(self, height, width, begin_y, begin_x):
        self.window = curses.newwin(height, width, begin_y, begin_x)
        self.height = height
        self.width = width
        self.window.keypad(True)

    def draw_segment(self, y, x):
        if x == self.width - 1 and y == self.height - 1:
            pass
        else:
            self.window.addstr(y, x, "*")

    def draw_fruit(self, y, x):
        if x == self.width - 1 and y == self.height - 1:
            pass
        else:
            self.window.addstr(y, x, "ó")

    def clear(self):
        self.window.clear()

    def refresh(self):
        self.window.refresh()

    def end(self, result):
        if result == 1:
            self.window.clear()
            string = "YOU LOST"
            self.window.addstr(
                self.height // 2, self.width // 2 - len(string) // 2, string)
            self.window.refresh()
