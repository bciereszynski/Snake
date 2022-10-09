import curses
from menu import Menu
from game import Game
# game terminal with static overlay and dynamic gamewindow
# screen != menu, to enable submenus


class Screen:
    def __init__(self, stdscreen, height, width, begin_y, begin_x):
        self.stdscr = stdscreen  # object of
        curses.curs_set(0)
        curses.noecho()
        curses.cbreak()

        # Gamewindow with attributes
        self.menuwin = curses.newwin(height, width, begin_y, begin_x)
        self.menuwin.keypad(True)

        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Snake")
        self.stdscr.refresh()

    def init_menu(self):
        game = Game(20, 20, 5, 5)
        submenu_items = [("beep", curses.beep), ("flash", curses.flash)]
        submenu = Menu(submenu_items, self.menuwin)

        main_menu_items = [
            ("game", game.test),
            ("flash", curses.flash),
            ("submenu", submenu.display),
        ]
        main_menu = Menu(main_menu_items, self.menuwin)
        main_menu.display()


class MyApp(object):
    def __init__(self, stdscreen):
        self.screen = stdscreen
        self.gameMenu = Screen(self.screen, 20, 20, 5, 5)
        self.gameMenu.init_menu()


if __name__ == "__main__":
    curses.wrapper(MyApp)
