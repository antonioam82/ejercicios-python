import curses
import time
import random
from curses import textpad

stdscr = curses.initscr()
curses.curs_set(0)
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

def main(stdscr):
    texto="CENTRE"
    sh, sw = stdscr.getmaxyx()
    posicion1=sh//2
    posicion2=sw//2
    #def main(stdscr):
    stdscr.addstr(posicion1,(posicion2)-((len(texto))//2),texto)
    wp=[]
    for i in range(12):
        n=random.randint(1,28)
        m=random.randint(1,116)
        stdscr.addstr(n,m,"*")
        wp.append((n,m))
    
    while True:
        key=stdscr.getch()
        if key==curses.KEY_RIGHT:
            posicion2=posicion2+1
            texto="RIGHT"
        elif key==curses.KEY_DOWN:
            posicion1=posicion1+1
            texto="DOWN"
        elif key==curses.KEY_LEFT:
            posicion2=posicion2-1
            texto="LEFT"
        elif key==curses.KEY_UP:
            posicion1=posicion1-1
            texto="UP"
        current_p=(posicion1,posicion2)
        if current_p in wp:
            stdscr.clear()
            texto="BOOOM!"
        #stdscr.clear()
        stdscr.addstr(posicion1,(posicion2)-((len(texto))//2),texto)
    
main(stdscr)

stdscr.refresh()
#time.sleep(1)
stdscr.clear()

curses.curs_set(1)
curses.echo()
curses.nocbrek()
stdscr.keypad(False)


curses.endwin()
