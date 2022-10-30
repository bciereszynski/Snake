
import curses
import os
from game_window import GameWindow
from menu import Menu
from logic.game import Game
from logic.settings import Settings

# game terminal with static overlay and dynamic gamewindow
# screen != menu, to enable submenus


class Screen:
    def __init__(self):
        # screen init
        self.stdscr = curses.initscr()
        self.settings = Settings()
        self.maxY, self.maxX = self.stdscr.getmaxyx()

        # curses init
        curses.curs_set(0)
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        curses.init_pair(1, 112, 28)

        # menu init
        self.beginMenu_x = self.calcCenter(self.maxX) - 12
        self.begin_y = 7
        self.menu_y, self.menu_x = 10, 25

        self.snakeASCII = ["      _    _                                      ",
                           "   ,-(|)--(|)-.                                   ",
                           "   \_   ..   _/                                   ",
                           "     \______/                                     ",
                           "       V  V                                  ____ ",
                           "       `.^^`.                               /^,--`",
                           "         \^^^\                             (^^\\  ",
                           "         |^^^|                  _,-._       \^^\\ ",
                           "        (^^^^\      __      _,-'^^^^^`.    _,'^^) ",
                           "         \^^^^`._,-'^^`-._.'^^^^__^^^^ `--'^^^_/  ",
                           "          \^^^^^ ^^^_^^^^^^^_,-'  `.^^^^^^^^_/    ",
                           "           `.____,-' `-.__.'        `-.___.'      "]

        self.layout()

    def calcCenter(self, size, msgSize=0):
        return size // 2 - msgSize // 2

    def layout(self):
        self.stdscr.clear()
        self.stdscr.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
        msg = "SNAKE v.1.0"
        self.stdscr.addstr(1, self.calcCenter(self.maxX, len(msg)), msg)
        msg = "DIFFICULTY: " + self.settings.getDifficulty()[0]
        self.stdscr.addstr(3, self.calcCenter(self.maxX, len(msg)), msg)
        msg = "MAP SIZE: " + self.settings.getMap()[0]
        self.stdscr.addstr(4, self.calcCenter(self.maxX, len(msg)), msg)
        msg = "IN-GAME SOUND: " + self.settings.getSound()
        self.stdscr.addstr(5, self.calcCenter(self.maxX, len(msg)), msg)
        x = 17
        for msg in self.snakeASCII:
            self.stdscr.addstr(x, self.calcCenter(self.maxX, len(msg)), msg)
            x = x + 1
        self.stdscr.refresh()

    '''
    Methods used by menu buttons
    '''

    def init_game(self):
        window = GameWindow(self.settings.getMap()[1], self.settings.getMap()[2],
                            self.begin_y, self.calcCenter(self.maxX, self.settings.getMap()[2]), self.settings.getDifficulty()[1])
        game = Game(window, self.settings)
        game.play()
        self.layout()

    def changeMap(self):
        self.settings.mapSwitch()
        self.layout()

    def changeDifficulty(self):
        self.settings.difficultySwitch()
        self.layout()

    def changeSound(self):
        self.settings.soundSwitch()
        self.layout()
    ####

    def init_menu(self):

        menuwin = curses.newwin(
            self.menu_y, self.menu_x, self.begin_y, self.beginMenu_x)
        menuwin.keypad(True)
        settings_items = [("CHANGE DIFFICULTY", self.changeDifficulty),
                          ("CHANGE MAP SIZE", self.changeMap),
                          ("ON/OFF SOUNDS", self.changeSound)]
        settings_submenu = Menu(settings_items, menuwin)

        main_menu_items = [
            ("GAME", self.init_game),
            ("SETTINGS", settings_submenu.display)
        ]
        main_menu = Menu(main_menu_items, menuwin)
        main_menu.display()
        self.layout()


class App(object):

    def __init__(self, stdscreen):
        self.gameMenu = Screen()
        self.gameMenu.init_menu()
        os._exit(os.X_OK)


if __name__ == "__main__":
    curses.wrapper(App)
