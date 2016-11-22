import curses
from curses import wrapper

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'managers'))
from cursesManager import CursesManager

def diagnose(stdscr):
    # Check terminal properties
    CursesManager.diagnose()
    return None

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
    title = "This is a title"
    message = "This is a fast message in x = 5 and y = 5"
    message2 = "\nThis is a fast message with CRLF at the beggining"
    message3 = "You can manually put the cursor in position 10, 11 and print a message"
    message4 = "You can insert this message"
    message5 = "And you can delete it!"
    message6 = "And delete each ch of this message"
    message7 = "You can fill all lines with a for bucle, this is the number: %d"
    message8 = "You can fill all spaces in a line with a for bucle"
    x = 5
    y = 5

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    cm.print_message_center(title, 2)
    cm.print_message_at(message, x, y)
    cm.print_message(message2)
    cm.set_cursor(10, 11)
    cm.print_message(message3)
    cm.waitforkey()
    cm.insertln(10)
    cm.print_message(message4)
    cm.waitforkey()
    cm.insertln(10)
    cm.print_message(message5)
    cm.insertln(11)
    cm.waitforkey()
    # Manually use curses:
    y_max, x_max = stdscr.getmaxyx()
    for i in range(0, y_max - 1):
        cm.print_message_at(message7 % i, 1, i)
    cm.waitforkey()
    cm.clearln(0)
    cm.clearln(1)
    cm.clearln(2)
    cm.print_message_at(message8, 0, 0)
    cm.set_cursor(0, 1)
    for i in range(0, x_max):
        cm.print_ch("+")
    cm.waitforkey()
    #cm.print_message_at(message6, 7, 7)
    #cm.waitforkey()
    #cm.delch(7, 6)
    #cm.waitforkey()
    #cm.delch(8, 7)
    #cm.waitforkey()
    #cm.delch(9, 7)
    #cm.waitforkey()
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
    message = " You can change background\n And write with different colors"
    message2 = "\n Change it!"
    message3 = "\n And change again!!"
    message4 = "\n And create a border"
    message5 = "\n Change it!"
    message6 = "\n And change again!!"

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

# Cursor usage
def step7(stdscr):
    message = "Cursor off"
    message2 = "Cursor on"
    message3 = "Cursor fast"

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    cm.print_message_at(message, 1, 1)
    cm.set_cursor_mode(0)
    cm.rwait(1)
    cm.waitforkey()
    cm.print_message_at(message2, 1, 2)
    cm.set_cursor_mode(1)
    cm.rwait(1)
    cm.waitforkey()
    cm.print_message_at(message3, 1, 3)
    cm.set_cursor_mode(2)
    cm.rwait(1)
    cm.waitforkey()
    cm.cleanup()
    return None

# Create a book
def step8(stdscr):
    title = "My first book"
    pages = []
    author = "vgonisanz"
    page1 = "This is my first page."
    page2 = "This is my second page."
    page3 = "This is my third page."
    page4 = "This is my last page."
    pages.append(page1)
    pages.append(page2)
    pages.append(page3)
    pages.append(page4)

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    cm.print_book(title, pages, author)
    cm.waitforkey()
    cm.cleanup()
    return None

def step9(stdscr):
    title = "My first menu"
    options = []
    option1 = "Option 1"
    option2 = "Option 2"
    option3 = "Option 3"
    options.append(option1)
    options.append(option2)
    options.append(option3)
    instructions = "Use arrow keys to move, ENTER to select, q or ESC to abort."

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    option_choose = cm.print_menu(title, options, instructions)
    cm.print_message_at("Option chosen: %s" % option_choose, 1, 6)
    cm.waitforkey()
    cm.cleanup()
    return None

# Window demo
def step10(stdscr):
    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    win0, win1, win2, win3 = cm.print_4windows()
    win0.refresh()
    win1.refresh()
    win2.refresh()
    win3.refresh()
    cm.set_current_window(win0)
    cm.waitforkey(0, 5)
    y_max, x_max = win3.getmaxyx()
    win3.addch(y_max - 2, x_max - 2, "f")
    win3.refresh()
    cm.waitforkey(0, 5)
    cm.cleanup()
    return None

# Create question and get answer
def step11(stdscr):
    question = "What is your name?"

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    answer = cm.print_question(question, True, 1, 1, 1, 2)
    cm.print_message(" Your answer was: " + answer)
    cm.waitforkey()
    cm.cleanup()
    return None

# Playing with cursor
def step12(stdscr):
    ch = "a"
    message = "Lets try use cursor"
    message_cursor = "Cursor at x=%d and y=%d"
    message_max = "win is width = %s and height = %s"

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    cm.print_message_center(message, 0)
    x_max, y_max = cm.get_max_cursor()
    # Invalid value
    x = -1
    y = -1
    # Corrected!
    x, y = cm.get_valid_cursor(x, y)
    cm.print_ch_at(ch, x, y, curses.A_REVERSE)
    # Where is? (1,0) after write a character
    x_cur, y_cur = cm.get_cursor()
    cm.print_message_at(message_cursor % (x_cur, y_cur), 1, 1)
    cm.waitforkey()
    # Invalid value
    x = 20000
    y = 20000
    # Corrected!
    x, y = cm.get_valid_cursor(x, y)
    cm.print_ch_at(ch, x, y, curses.A_REVERSE)
    # Where is? after write a character
    x_cur, y_cur = cm.get_cursor()
    cm.print_message_at(message_cursor % (x_cur, y_cur), 1, 2)
    cm.waitforkey()
    # Valid value
    x = (int)(x_max/2)
    y = (int)(y_max/2)
    # Corrected!
    x, y = cm.get_valid_cursor(x, y)
    cm.print_ch_at(ch, x, y, curses.A_REVERSE)
    # Where is? in the middle after write a character
    x_cur, y_cur = cm.get_cursor()
    cm.print_message_at(message_cursor % (x_cur, y_cur), 1, 3)
    cm.waitforkey()
    cm.cleanup()
    return None

def step13(stdscr):
    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    title = "This is a progress bar"
    progress = 0
    bar_width = 30
    cm.print_message_at(title, 5, 5)
    while progress <= 100:
        cm.print_progress_bar(progress, 5, 6, bar_width)
        progress = progress + 1
        cm.rwait(100)
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
    # Configuration
    curses.echo()
    curses.curs_set(1)
    curses.setsyx(10, 10)
    curses.doupdate()
    # Click put, clicky, mouse diagnose
    # paint sith matrix or lists
    # Secure print no out of bounds?

if __name__ == "__main__":
    #wrapper(diagnose)
    #wrapper(step1)
    #wrapper(step2)
    #wrapper(step3)
    #wrapper(step4)
    #wrapper(step5)
    #wrapper(step6)
    #wrapper(step7)
    #wrapper(step8)
    #wrapper(step9)
    #wrapper(step10)
    #wrapper(step11)
    #wrapper(step12)
    wrapper(step13)
    print("Thanks for using curses guide")

# TODO Check create pads
