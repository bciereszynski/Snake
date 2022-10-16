import curses
import os
from game_window import GameWindow
from menu import Menu
from game import Game
from settings import Settings
# game terminal with static overlay and dynamic gamewindow
# screen != menu, to enable submenus


class Screen:
    def __init__(self, stdscreen):
        self.stdscr = curses.initscr()  # object of screen
        self.begin_x = 6
        self.begin_y = 6
        self.menuSize = 20
        curses.curs_set(0)
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

        self.settings = Settings()

        # Menu window
        self.menuwin = curses.newwin(
            self.menuSize, self.menuSize, self.begin_y, self.begin_x)
        self.menuwin.keypad(True)
        self.layout()

        # TODO layout
    def layout(self):
        self.stdscr.clear()
        self.stdscr.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
        self.stdscr.addstr(1, (self.menuSize) // 2 + 2, "SNAKE v.1.0")
        self.stdscr.addstr(3, 5, "DIFFICULTY: " +
                           self.settings.getDifficulty()[0]);
        self.stdscr.addstr(4, 5, "MAP SIZE: " +
                           self.settings.getMap()[0]);
        self.stdscr.refresh()

    def init_game(self):
        window = GameWindow(self.settings.getMap()[1], self.settings.getMap()[2],
                             self.begin_y, self.begin_x, self.settings.getDifficulty()[1])
        game = Game(window)
        game.play()
        self.layout()
        pointsMsg =  str(game.points) + " points"
        self.menuwin.addstr(8,5,"GAMEOVER!")
        self.menuwin.addstr(9,5,pointsMsg)

    def changeMap(self):
        self.settings.mapSwitch()
        self.layout()

    def changeDifficulty(self):
        self.settings.difficultySwitch()
        self.layout()

    ##TODO you lose/your points

    def init_menu(self):
        # TODO Settings menu - changes in layout
        settings_items = [("CHANGE DIFFICULTY", self.changeDifficulty),
                          ("CHANGE MAP SIZE", self.changeMap)]
        settings_submenu = Menu(settings_items, self.menuwin)

        main_menu_items = [
            ("GAME", self.init_game),
            ("SETTINGS", settings_submenu.display)
        ]
        main_menu = Menu(main_menu_items, self.menuwin)
        main_menu.display()


class App(object):
    def __init__(self, stdscreen):
        self.screen = stdscreen
        self.gameMenu = Screen(self.screen)
        self.gameMenu.init_menu()
        os._exit(os.X_OK)


if __name__ == "__main__":
    curses.wrapper(App)
