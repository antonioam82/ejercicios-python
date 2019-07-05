import time
import curses
import random

stdscr=curses.initscr()

curses.curs_set(0)
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

for i in ["Hello","my","friend!"]:
    try:
        n=random.randint(1,40)
        m=random.randint(1,100)
        stdscr.addstr(n,m,i)
    except:
        stdscr.addstr(15,5,"We have a problem here")
    
    stdscr.refresh()
    time.sleep(4)
    stdscr.clear()

curses.curs_set(1)
curses.echo()
curses.nocbrek()
stdscr.keypad(False)

curses.endwin()
