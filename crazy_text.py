import time
import curses
import random

stdscr=curses.initscr()

curses.curs_set(0)
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

for i in ["Este","es","un","sencillo","ejemplo","de",
          "prueba","espero","que","te","guste"]:
    try:
        n=random.randint(1,28)#25
        m=random.randint(1,116)#125
        stdscr.addstr(n,m,i)
    except:
        stdscr.addstr(5,15,"We have a problem here")#15,5
    
    stdscr.refresh()
    time.sleep(1)
    stdscr.clear()

curses.curs_set(1)
curses.echo()
curses.nocbrek()
stdscr.keypad(False)

curses.endwin()
