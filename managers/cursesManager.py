#from __future__ import unicode_literals # Unicode python2.7 test
import curses
from curses import wrapper

import locale
import types

"""
This python 3 class will manager a curses windows for you.

To generate HTML documentation for this module issue the command:

    pydoc -w cursesManager

"""

class CursesManager(object):
    _current_window = None

    """
    Initialize CursesManager
    """
    @classmethod
    def __init__(self, echo=False):
        print("Initializing curses Manager")
        # Set UTF-8
        locale.setlocale(locale.LC_ALL, '')
        code = locale.getpreferredencoding()
        return

    """
    Enter CursesManager
    """
    @classmethod
    def __enter__(self):
        print("Enter curses Manager")
        return self

    """
    Exit CursesManager
    """
    @classmethod
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit curses Manager")
        curses.endwin()
        return None

    """
    Print info.

    :return: returns nothing
    """
    @classmethod
    def init(self):
        print("Init basic stuffs")
        curses.start_color()
        return None

    """
    Diagnose terminal and print info. Static, you can use githout instance.
    Give all info about curses and you terminal. Use it at the beginning to test.

    :return: returns nothing
    """
    @staticmethod
    def diagnose():
        window = curses.initscr()
        window.addstr("\n  Userful info:")
        window.addstr("\n  Terminal: %s" % curses.longname())
        window.addstr("\n  Can use color: %s" % curses.has_colors())
        if curses.has_colors():
            window.addstr("\n  Can change colors: %s" % curses.can_change_color())
            window.addstr("\n  Terminal has %s colors" % curses.COLORS)
            window.addstr("\n  Terminal has %s pairs of colors" % curses.COLOR_PAIRS)
        window.addstr("\n  Number of lines: %s (y size) " % curses.LINES)
        window.addstr("\n  Number of cols: %s (x size)" % curses.COLS)
        window.border()
        window.getkey()
        curses.endwin()
        return None

    """
    Create window object.

    :return: returns nothing
    """
    @classmethod
    def create_window(self, width = 20, height = 20):
        print("Creating window with size: %sx%s" % (width, height))
        return None

    """
    Draw an object.

    :return: returns nothing
    """
    @classmethod
    def draw(self):
        print("Drawing...")
        #self._stdscr.addsrt(0, 0, "Hi!")
        #self._stdscr.refresh()
        return None

    """
    Close curses object.

    :return: returns nothing
    """
    @classmethod
    def cleanup(self):
        curses.endwin()
        print("Cleaning up...")
        return None

    """
    Set current window to work. Use before print any message

    :return: returns nothing
    """
    @classmethod
    def set_current_window(self, stdscr):
        self._current_window = stdscr
        return None

    """
    Clear current window.

    :return: returns nothing
    """
    @classmethod
    def clear(self):
        if self._current_window != None:
            self._current_window.clear()
        return None

    """
    Get a key.

    :return: returns None
    """
    @classmethod
    def getkey(self):
        if self._current_window != None:
            return self._current_window.getkey()
        return None

    """
    Get a char.

    :return: returns character with key
    """
    @classmethod
    def getch(self):
        if self._current_window != None:
            return self._current_window.getch()
        return None

    """
    Wait for key.

    :return: returns None
    """
    @classmethod
    def waitforkey(self, x0 = -1, y0 = -1):
        if self._current_window != None:
            self.rwait(1)
            if x0 > -1 and y0 > -1:
                self.set_cursor(x0, y0)
            self.print_message("\n Press any key to continue.")
            return self._current_window.getkey()
        return None

    """
    Refresh screen and wait time in milliseconds.

    :return: returns None
    """
    @classmethod
    def rwait(self, ms = 1):
        if self._current_window != None:
            self._current_window.refresh()
        curses.napms(ms)
        return None

    """
    Set cursor at position.

    :return: returns None
    """
    @classmethod
    def set_cursor(self, x0, y0):
        if self._current_window != None:
            self._current_window.move(y0, x0)
        return None

    """
    Set cursor mode.

    :return: returns None
    """
    @classmethod
    def set_cursor_mode(self, mode):
        if mode >= 0 and mode < 3:
            curses.curs_set(mode)
        return None

    """
    Clear line y.

    :return: returns None
    """
    @classmethod
    def clearln(self, y0):
        if self._current_window != None:
            self._current_window.move(y0, 0)
            self._current_window.clrtoeol()
        return None

    """
    Clear line from (x, y) position.

    :return: returns None
    """
    @classmethod
    def clrtoeol(self, x0, y0):
        if self._current_window != None:
            self._current_window.move(y0, x0)
            self._current_window.clrtoeol()
        return None

    """
    Clear terminal from (x, y) position.

    :return: returns None
    """
    @classmethod
    def clrtobot(self, x0, y0):
        if self._current_window != None:
            self._current_window.move(y0, x0)
            self._current_window.clrtobot()
        return None

    """
    Clear terminal from (x, y) position.

    :return: returns None
    """
    @classmethod
    def flash(self):
        curses.flash()
        return None

    """
    Request insert next line, moving down data

    :return: returns None
    """
    @classmethod
    def insertln(self, y0):
        if self._current_window != None:
            self._current_window.move(y0, 0)
            self._current_window.insertln()
        return None

    """
    Request delete line at line y

    :return: returns None
    """
    @classmethod
    def deleteln(self, y0 = -1):
        if self._current_window != None:
            if y0 >= 0:
                self._current_window.move(y0, 0)
            self._current_window.deleteln()
        return None

    """
    Request delete character at position x0, y0

    :return: returns None
    """
    @classmethod
    def delch(self, x0, y0):
        if self._current_window != None:
            self._current_window.delch(y0, x0)
        return None

    """
    Print background with color.

    :return: returns nothing
    """
    @classmethod
    def print_background(self, color_character, color_background):
        if self._current_window != None:
            # Set color
            curses.init_pair(7, color_character, color_background);
            # Draw background
            self._current_window.bkgd(curses.color_pair(7));
            self.rwait(1)
        return None

    """
    Print border with elements.

    :return: returns nothing
    """
    @classmethod
    def print_border(self, type = 0):
        if self._current_window != None:
            # Set border
            if type == 0:
                self._current_window.border()
            elif type == 1:
                self._current_window.border(curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_BLOCK, curses.ACS_BLOCK, curses.ACS_BLOCK, curses.ACS_BLOCK)
            elif type == 2:
                self._current_window.border("|", "|", "-", "-", "x", "x", "x", "x")
            else:
                ls = "X"
                rs = "X"
                ts = "X"
                bs = "X"
                tl = "X"
                tr = "X"
                bl = "X"
                br = "X"
                self._current_window.border(ls, rs, ts, bs, tl, tr, bl, br)
            self.rwait(1)
        return None

    """
    Print background with a pattern from (0, 0).

    :return: returns nothing
    """
    @classmethod
    def fill_with_pattern(self, pattern):
        if self._current_window != None:
            y_max, x_max = self._current_window.getmaxyx()
            lenght = len( pattern )
            times = (int)(x_max * (y_max  -1) / lenght) - 1
            self._current_window.move(0, 0)
            for i in range(0, times):
                self.print_message(pattern)
            self.rwait(1)
        return None

    """
    Print a character string at current cursor position.

    :return: returns nothing
    """
    @classmethod
    def print_ch(self, ch, attributes = curses.A_NORMAL):
        if self._current_window != None:
            # Set attributes
            self._current_window.attrset(attributes)
            # Print
            self._current_window.addch(ch)
            # Restore attributes
            self._current_window.attroff(attributes)
        return None

    """
    Print a message string at current cursor position.

    :return: returns nothing
    """
    @classmethod
    def print_message(self, message, attributes = curses.A_NORMAL):
        if self._current_window != None:
            # Set attributes
            self._current_window.attrset(attributes)
            # Print
            self._current_window.addstr(message)
            # Restore attributes
            self._current_window.attroff(attributes)
        return None

    """
    Print a message string at y position centered.

    :return: returns nothing
    """
    @classmethod
    def print_message_center(self, message, y0, attributes = curses.A_NORMAL):
        if self._current_window != None:
            y_max, x_max = self._current_window.getmaxyx()
            lenght = len( message )
            indent = x_max - lenght
            indent = (int)(indent / 2)
            y0_int = (int)(y0)

            # Set attributes
            self._current_window.attrset(attributes)
            # Set cursor
            self.set_cursor(indent, y0_int)
            # Print
            self._current_window.addstr(message)
            # Restore attributes
            self._current_window.attroff(attributes)
        return None

    """
    Print a message slow with delay between character at cursor position.

    :return: returns nothing
    """
    @classmethod
    def print_message_slow(self, message, inter_delay = 100, attributes = curses.A_NORMAL):
        if self._current_window != None:
            # Set attributes
            self._current_window.attrset(attributes)
            for char in message:
                self._current_window.addch(char)
                self._current_window.refresh()
                curses.napms(inter_delay)
            # Restore attributes
            self._current_window.attroff(attributes)
        return None

    """
    Print a message string at position.

    :return: returns nothing
    """
    @classmethod
    def print_message_at(self, message, x0 = 0, y0 = 0, attributes = curses.A_NORMAL):
        if self._current_window != None:
            # Set attributes
            self._current_window.attrset(attributes)
            # Set cursor position
            self._current_window.move(y0, x0)
            # Print
            self._current_window.addstr(message)
            # Restore attributes
            self._current_window.attroff(attributes)
        return None

    """
    Print a message with delay between character. It cannot be skipped.

    :return: returns nothing
    """
    @classmethod
    def print_message_slow_at(self, message, x0 = 0, y0 = 0, inter_delay = 100, attributes = curses.A_NORMAL):
        if self._current_window != None:
            # Set attributes
            self._current_window.attrset(attributes)
            # Set cursor position
            self._current_window.move(y0, x0)
            for char in message:
                self._current_window.addch(char)
                self._current_window.refresh()
                curses.napms(inter_delay)
            # Restore attributes
            self._current_window.attroff(attributes)
        return None

    """
    Print book like.

    :return: returns nothing
    """
    @classmethod
    def print_book(self, title, pages, author = ""):
        if self._current_window != None:
            y_max, x_max = self._current_window.getmaxyx()
            mid_y = (int)(y_max / 2)
            q_y = (int)(y_max * 3/4)
            q_x = (int)(x_max * 3/4)
            # Print title, author, and wait
            self.clear()
            self.print_message_center(title, mid_y)
            self.print_message_at(author, q_x, q_y)
            self.print_border()
            self.waitforkey()
            # Read each page
            for page in pages:
                self.clear()
                self.print_message_at(page, 1,1)
                self.print_border()
                self.waitforkey()
            # End
            self.clear()
            self.print_message_center("The end", y/2)
            self.print_border()
            self.waitforkey()
        return None

    """
    Print menu like.

    :return: returns -1 if quit with q or ESC, option id from [0, N-1] if ENTER
    """
    @classmethod
    def print_menu(self, title, options, instructions = ""):
        if len(options) <= 0:
            return None
        option_selected = 0
        quit_menu = False
        if self._current_window != None:
            self.__draw_menu(title, options, option_selected, instructions)
            while not quit_menu:
                event = self.getch()
                if event == curses.KEY_UP:
                    option_selected = option_selected - 1
                if event == curses.KEY_DOWN:
                    option_selected = option_selected + 1
                if event == curses.KEY_ENTER or event == 10 or event == 13:
                    quit_menu = True
                option_selected = self.__draw_menu(title, options, option_selected, instructions)
                if event == ord('q') or event == 28:
                    quit_menu = True
                    option_selected = -1
        return option_selected

    """
    Draw menu options.

    :return: returns option selected
    """
    @classmethod
    def __draw_menu(self, title, options, option_selected, instructions, offset_x = 15, offset_y = 0, title_padding = 1, instruction_padding = 1):
        max_options = len(options)
        if option_selected < 0:
            option_selected = 0
        if option_selected >= max_options:
            option_selected = max_options - 1
        counter = 0
        self.print_message_at(title, offset_x, offset_y, curses.A_UNDERLINE)
        for option in options:
            if option_selected == counter:
                self.print_message_at(option, offset_x, counter + offset_y + title_padding + 1, curses.A_REVERSE)
            else:
                self.print_message_at(option, offset_x, counter + offset_y + title_padding + 1)
            counter = counter + 1
        self.print_message_at(instructions, offset_x, counter + offset_y + title_padding + instruction_padding + 1)
        return option_selected

    """
    print 4 windows in a box.

    :return: returns win0, win1, win2, win3
    """
    @classmethod
    def print_4windows(self):
        y_max, x_max = self._current_window.getmaxyx()
        y_2 = y_max / 2
        x_2 = x_max / 2
        win0 = curses.newwin(y_2, x_2, 0, 0)
        win1 = curses.newwin(y_2, x_2, 0, x_2)
        win2 = curses.newwin(y_2, x_2, y_2, 0)
        win3 = curses.newwin(y_2, x_2, y_2, x_2)
        self.rwait(1)
        win0.addstr(1, 1, "Window 0")
        win1.addstr(1, 1, "Window 1")
        win2.addstr(1, 1, "Window 2")
        win3.addstr(1, 1, "Window 3")
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE);
        win0.bkgd(curses.color_pair(2))
        win0.border()
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE);
        win1.bkgd(curses.color_pair(3))
        win1.border()
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_WHITE);
        win2.bkgd(curses.color_pair(4))
        win2.border()
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN);
        win3.bkgd(curses.color_pair(5))
        win3.border()
        return win0, win1, win2, win3

    """
    Template.

    :return: returns nothing
    """
    @classmethod
    def template(self):
        #
        return None
