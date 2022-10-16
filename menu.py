
import curses
import winsound
from curses import panel


class Menu(object):
    def __init__(self, items, window):
        self.window = window
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 0
        self.items = items
        self.items.append(("EXIT", "EXIT"))

    def navigate(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= len(self.items):
            self.position = len(self.items) - 1

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True:
            for index, item in enumerate(self.items):
                # reverse - highlighted option
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = " %s" % (item[0])
                self.window.addstr(1 + index, 1, msg, mode)

            self.window.refresh()
            curses.doupdate()

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord("\n")]:
                winsound.Beep(300, 100)
                self.window.clear()
                if self.position == len(self.items) - 1:
                    break
                else:
                    self.items[self.position][1]()
                    self.window.refresh()

            elif key == curses.KEY_UP:
                self.navigate(-1)

            elif key == curses.KEY_DOWN:
                self.navigate(1)

        self.panel.hide()
        curses.doupdate()
