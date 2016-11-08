from curses import wrapper
import curses
from curses.textpad import Textbox, rectangle

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 9):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

    begin_x = 20; begin_y = 7
    height = 5; width = 40
    win = curses.newwin(height, width, begin_y, begin_x)

    pad = curses.newpad(100, 100)
    # These loops fill the pad with letters; addch() is
    # explained in the next section
    for y in range(0, 99):
        for x in range(0, 99):
            pad.addch(y,x, ord('a') + (x*x+y*y) % 26)

    # Displays a section of the pad in the middle of the screen.
    # (0,0) : coordinate of upper-left corner of pad area to display.
    # (5,5) : coordinate of upper-left corner of window area to be filled
    #         with pad content.
    # (20, 75) : coordinate of lower-right corner of window area to be
    #          : filled with pad content.
    pad.refresh( 0,0, 5,5, 20,75)

    stdscr.getkey()
    return None

def test(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Current mode: Typing mode",
              curses.A_BLINK)
    stdscr.addstr(1, 0, "Current mode: Typing mode",
              curses.A_BOLD)
    stdscr.addstr(2, 0, "Current mode: Typing mode",
              curses.A_DIM)
    stdscr.addstr(3, 0, "Current mode: Typing mode",
              curses.A_REVERSE)
    stdscr.addstr(4, 0, "Current mode: Typing mode",
              curses.A_STANDOUT)
    stdscr.addstr(5, 0, "Current mode: Typing mode",
              curses.A_UNDERLINE)
    stdscr.addstr(6, 0, "Current mode: Typing mode",
              curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getkey()
    return None

def test2(stdscr):
    curses.start_color()
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    stdscr.addstr(1, 0, "Pretty text", curses.color_pair(2))
    stdscr.addstr(0,0, "RED ALERT!", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey()
    curses.echo()            # Enable echoing of characters
    # Get a 15-character string, with the cursor on the top line
    s = stdscr.getstr(0,0, 15)
    print("Get: %s" % s)
    stdscr.getkey()
    #process(stdscr)
    return None

def test3(stdscr):
    stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")

    editwin = curses.newwin(5,30, 2,1)
    #infowin = curses.newwin(5,30, 5,1)
    rectangle(stdscr, 1, 0, 1+5+1, 1+30+1)
    #rectangle(stdscr, 1, 0, 1+5+1, 1+30+1)
    stdscr.refresh()


    box = Textbox(editwin)
    #boxinfo = Textbox(infowin)

    # Let the user edit until Ctrl-G is struck.
    box.edit()

    # Get resulting contents
    message = box.gather()
    print(message)
    stdscr.refresh()
    stdscr.getkey()
    return

def init(stdscr):
    # don't echo key strokes on the screen
    curses.noecho()
    # read keystrokes instantly, without waiting for enter to ne pressed
    curses.cbreak()
    # enable keypad mode
    stdscr.keypad(1)
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(False)
    curses.init_pair(1, curses.COLOR_RED,     curses.COLOR_BLACK);
    curses.init_pair(2, curses.COLOR_GREEN,   curses.COLOR_BLACK);
    curses.init_pair(3, curses.COLOR_YELLOW,  curses.COLOR_BLACK);
    curses.init_pair(4, curses.COLOR_BLUE,    curses.COLOR_BLACK);
    curses.init_pair(5, curses.COLOR_CYAN,    curses.COLOR_BLACK);
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK);
    curses.init_pair(7, curses.COLOR_WHITE,   curses.COLOR_BLACK);
    return None

def test4(stdscr):
    init(stdscr)
    #
    initial_coordinates = stdscr.getparyx()
    size = stdscr.getmaxyx()
    initial_coordinates_message = "Initial (x, y): " + str(initial_coordinates[1]) + " " + str(initial_coordinates[0])
    size_message = "Size (x, y): " + str(size[1]) + " " + str(size[0])
    # Draw
    #
    #curses.textpad.rectangle(main_window, 0, 0, size[0] - 2, size[1] - 2)
    #main_window.addstr(0, 2, "Main window")
    main_window = draw_window(0, 0, size[1], size[0], "Main window")
    main_window.addstr(1, 2, initial_coordinates_message)
    main_window.addstr(2, 2, size_message)
    window = draw_window(size[0]/2, 5, size[1]/2, size[0]/4, "Sub window")
    #window = curses.newwin(20, 20, 5, 5)
    #curses.textpad.rectangle(window, 0, 0, 5, 5)

    #draw_window(5, 5, 20, 20, "Sub window")

    main_window.refresh()
    window.refresh()
    main_window.getkey()
    #edit_textbox = maketextbox(main_window, 3, 10, 5, 5, 1)
    #edit_textbox.edit()
    #main_window.getkey()

def draw_window(x0, y0, w, h, title = ""):
    # newwin(nlines, ncols, begin_y, begin_x)
    # rectangle(win, uly, ulx, lry, lrx)
    window = curses.newwin(h, w, y0, x0)
    uly = y0
    ulx = x0
    lry = h - y0 - 2
    lrx = w - x0 - 2
    #curses.textpad.rectangle(window, uly, ulx, lry, lrx ) # = border 0
    window.border(0)
    window.addstr(0, 0 + 2, title)
    return window

def maketextbox(h, w, y, x, title = "", margin = 1):
    nw = curses.newwin(h,w,y,x)
    txtbox = curses.textpad.Textbox(nw)
    if deco=="frame":
        screen.attron(decoColorpair)
        curses.textpad.rectangle(screen,y-1,x-1,y+h,x+w)
        screen.attroff(decoColorpair)
    elif deco=="underline":
        screen.hline(y+1,x,underlineChr,w,decoColorpair)

    nw.addstr(0,0,value,textColorpair)
    nw.attron(textColorpair)
    screen.refresh()
    return txtbox

def process(stdscr):
    while True:
        c = stdscr.getch()
        if c == ord('p'):
            print("im printing")
        elif c == ord('q'):
            print("Ending")
            break  # Exit the while loop
        elif c == curses.KEY_HOME:
            x = y = 0


#wrapper(main)
#wrapper(test2)
wrapper(test4)
