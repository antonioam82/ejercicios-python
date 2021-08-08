import pygame as pg
from OpenGL.GL import *

class App:
    def __init__(self):
        pg.init()
        pg.display.set_mode((640,480), pg.OPENGL|pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        

        #glClearColor(0.0,0.0,1.0,1.0)
        glClearColor(0, 0, 1, 1)
        self.mainloop()
        print("hello")

    def mainloop(self):
        running = True
        while(running):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()

            self.clock.tick()
            framerate = int(self.clock.get_fps())
            pg.display.set_caption(f"Running at {framerate} fps.")

        self.quit()

    def quit(self):
        pg.quit()

        
if __name__=="__main__":
    App()
