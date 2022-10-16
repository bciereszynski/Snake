import curses
from game_window import GameWindow
from menu import Menu
from game import Game
# game terminal with static overlay and dynamic gamewindow
# screen != menu, to enable submenus


class Screen:
    def __init__(self, stdscreen, height, width, begin_y, begin_x):
        self.stdscr = stdscreen  # object of screen
        curses.curs_set(0)
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
        self.stdscr.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)

        # Menu window
        self.menuwin = curses.newwin(height, width, begin_y, begin_x)
        self.menuwin.keypad(True)

        # TODO layout
        self.stdscr.clear()
        self.stdscr.addstr(1, (width) // 2 + 2, "Snake")
        self.stdscr.refresh()

    def init_game(self):
        window = GameWindow(20, 20, 5, 5)
        game = Game(window)
        game.play()

    def init_menu(self):
        # TODO Settings menu
        submenu_items = [("beep", curses.beep), ("flash", curses.flash)]
        submenu = Menu(submenu_items, self.menuwin)

        main_menu_items = [
            ("game", self.init_game),
            ("flash", curses.flash),
            ("submenu", submenu.display),
        ]
        main_menu = Menu(main_menu_items, self.menuwin)
        main_menu.display()


class App(object):
    def __init__(self, stdscreen):
        self.screen = stdscreen
        self.gameMenu = Screen(self.screen, 20, 20, 5, 5)
        self.gameMenu.init_menu()


if __name__ == "__main__":
    curses.wrapper(App)
