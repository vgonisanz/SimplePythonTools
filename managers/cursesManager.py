import curses
from curses import wrapper

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
    Print info.

    :return: returns nothing
    """
    @classmethod
    def print_info(self):
        print("Lines: %s (y size) " % curses.LINES)
        print("Cols: %s (x size)" % curses.COLS)
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

    :return: returns string with key
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

    :return: returns string with key
    """
    @classmethod
    def waitforkey(self):
        if self._current_window != None:
            self.rwait(1)
            self.print_message("\nPress any key to continue.")
            return self._current_window.getkey()
        return None

    """
    Refresh screen and wait time in milliseconds.

    :return: returns string with key
    """
    @classmethod
    def rwait(self, ms = 1):
        if self._current_window != None:
            self._current_window.refresh()
        curses.napms(ms)
        return None

    """
    Set cursor at position.

    :return: returns string with key
    """
    @classmethod
    def set_cursor(self, x0, y0):
        if self._current_window != None:
            self._current_window.move(y0, x0)
        return None

    """
    Clear line from (x, y) position.

    :return: returns string with key
    """
    @classmethod
    def clrtoeol(self, x0, y0):
        if self._current_window != None:
            self._current_window.move(y0, x0)
            self._current_window.clrtoeol()
        return None

    """
    Clear terminal from (x, y) position.

    :return: returns string with key
    """
    @classmethod
    def clrtobot(self, x0, y0):
        if self._current_window != None:
            self._current_window.move(y0, x0)
            self._current_window.clrtobot()
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
            y, x = self._current_window.getmaxyx()
            lenght = len( pattern )
            times = (x * (y - 1) / lenght) - 1 # Without -1 can fail with 5 elements
            self._current_window.move(0, 0)
            for i in range(0, times):
                self.print_message(pattern)
            self.rwait(1)
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
