import curses
from curses import wrapper

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'managers'))
from cursesManager import CursesManager

# Create slow text
def step1(stdscr):
    message = "Welcome to this guide. Press any key"

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    cm.print_message_slow_at(message)
    cm.waitforkey()
    cm.cleanup()
    return None

# Create text at position
def step2(stdscr):
    message = "This is a fast message in x = 5 and y = 5"
    message2 = "\nThis is a fast message with CRLF at the beggining"
    message3 = "You can manually put the cursor in position 10, 11 and print a message"
    x = 5
    y = 5

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    cm.print_message_at(message, x, y)
    cm.print_message(message2)
    cm.set_cursor(10, 11)
    cm.print_message(message3)
    cm.waitforkey()
    cm.cleanup()
    return None

# Use attributes
def step3(stdscr):
    message = "Lets play with attributes:\n"
    options = "You can combine: A_ALTCHARSET, A_BLINK, A_BOLD, A_DIM, A_NORMAL, A_REVERSE, A_STANDOUT , A_UNDERLINE\n"
    alternate = " Alternate\n"
    blink = " Blink\n"
    bold = " Bold\n"
    dim = " Dim\n"
    normal = " Normal\n"
    reverse = " Reverse\n"
    standard = " Standard\n"
    underline = " Underline\n"
    mix = " mix mix mix "

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    cm.print_message(message)
    cm.print_message(options)
    cm.rwait(1000)
    cm.print_message(alternate, curses.A_ALTCHARSET)
    cm.rwait(300)
    cm.print_message(blink, curses.A_BLINK)
    cm.rwait(300)
    cm.print_message(bold, curses.A_BOLD)
    cm.rwait(300)
    cm.print_message(dim, curses.A_DIM)
    cm.rwait(300)
    cm.print_message(normal, curses.A_NORMAL)
    cm.rwait(300)
    cm.print_message(reverse, curses.A_REVERSE)
    cm.rwait(300)
    cm.print_message(standard, curses.A_STANDOUT)
    cm.rwait(300)
    cm.print_message(underline, curses.A_UNDERLINE)
    cm.waitforkey()
    cm.cleanup()
    return None

# Getch bucle
def step4(stdscr):
    message = "Example iterator:\n Push any arrow to print a message, quit with 'q'\n"

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    cm.print_message(message)
    condition = True
    while condition:
        event = cm.getch()
        if event == curses.KEY_LEFT:
            cm.print_message("Left\n")
        if event == curses.KEY_RIGHT:
            cm.print_message("Right\n")
        if event == curses.KEY_UP:
            cm.print_message("Up\n")
        if event == curses.KEY_DOWN:
            cm.print_message("Down\n")
        if event == curses.KEY_BACKSPACE:
            cm.print_message("Backspace\n")
        if event == ord('q'):
            cm.print_message("Quit command\n")
            cm.rwait(300)
            condition = False
    cm.waitforkey()
    cm.cleanup()
    return None

def step5(stdscr):
    message = "You can change background\nAnd write with different colors"
    message2 = "\nChange it!"
    message3 = "\nAnd change again!!"
    message4 = "\nAnd create a border"
    message5 = "\nChange it!"
    message6 = "\nAnd change again!!"

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.init()
    cm.clear()
    cm.print_background(curses.COLOR_WHITE, curses.COLOR_BLUE)
    cm.print_message(message)
    cm.waitforkey()
    cm.print_background(curses.COLOR_RED, curses.COLOR_GREEN)
    cm.print_message(message2)
    cm.waitforkey()
    cm.print_background(curses.COLOR_YELLOW, curses.COLOR_MAGENTA)
    cm.print_message(message3)
    cm.waitforkey()
    cm.print_background(curses.COLOR_WHITE, curses.COLOR_BLUE)
    cm.print_message(message4)
    cm.print_border(0)
    cm.waitforkey()
    cm.print_message(message5)
    cm.print_border(1)
    cm.waitforkey()
    cm.print_message(message6)
    cm.print_border(2)
    cm.waitforkey()
    cm.cleanup()
    return None

# Selective clear
def step6(stdscr):
    message = "Fill and clear.\n1.- Let's put text in all terminal"
    message2 = "2.- Let's clean from (4, 5) to end of line"
    message3 = "3.- Let's clean from (6, 7) to end of terminal"

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    cm.print_message(message)
    cm.waitforkey()
    cm.fill_with_pattern("#===#")
    cm.waitforkey()
    cm.print_message_at(message2, 0, 0)
    cm.clrtoeol(4, 5)
    cm.waitforkey()
    cm.print_message_at(message3, 0, 0)
    cm.clrtobot(6, 7)
    cm.waitforkey()
    cm.cleanup()
    return None

def step7(stdscr):
    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()

    cm.waitforkey()
    cm.cleanup()
    return None

def template(stdscr):
    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()

    cm.waitforkey()
    cm.cleanup()
    return None

def tryit():
    curses.echo()
    curses.curs_set(1)
    curses.setsyx(10, 10)
    curses.doupdate()

if __name__ == "__main__":
    #wrapper(step1)
    #wrapper(step2)
    #wrapper(step3)
    #wrapper(step4)
    wrapper(step5)
    #wrapper(step6)
    #wrapper(step7)
    #wrapper(step5)
    #wrapper(step5)
    #wrapper(step5)
    print("Thanks for using curses guide")

# TODO Check create pads
