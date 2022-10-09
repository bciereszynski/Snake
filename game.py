import curses
from curses import panel


class Game:
    def __init__(self, height, width, begin_y, begin_x):
        self.window = curses.newwin(height, width, begin_y, begin_x)
        self.window.keypad(True)

    def test(self):
        self.window.addstr(1, 1, "cos")
        self.window.refresh()
        self.window.getch()
