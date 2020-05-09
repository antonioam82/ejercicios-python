import glfw
from OpenGL.GL import *
import numpy as np

class Window:
    def __init__(self, width:int, height:int, title:str):
        if not glfw.init():
            raise Exception("glfw can not be initialized")

        self._win = glfw.create_window(width, height, title, None, None)

        if not self._win:
            glfw.terminate()
            raise Exception("glfw window can not be created")

        glfw.set_window_pos(self._win, 400, 200)
        glfw.make_context_current(self._win)

        vertices = [-0.5, -0.5, 0.0,
                     0.5, -0.5, 0.0,
                     0.0,  0.5, 0.0]

        colors = [1.0, 0.0, 0.0,
                  0.0, 1.0, 0.0,
                  0.0, 0.0, 1.0]
        
        vertices = np.array(vertices, dtype=np.float32)
        colors = np.array(colors, dtype=np.float32)

        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, vertices)

        glEnableClientState(GL_COLOR_ARRAY)
        glColorPointer(3, GL_FLOAT, 0, colors)
        
        glClearColor(0, 0.1, 0.1, 1)

    def main_loop(self):
        while not glfw.window_should_close(self._win):
            glfw.poll_events()
            
            glClearColor(0, 0, 0, 0)
            glClear(GL_COLOR_BUFFER_BIT)

            glDrawArrays(GL_TRIANGLES, 0, 3)

            glfw.swap_buffers(self._win)

        glfw.terminate()

if __name__ == "__main__":
    win = Window(1100, 720, "My OpenGL window")#1280, 720,
    win.main_loop()
            
