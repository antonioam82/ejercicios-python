import glfw
from OpenGL.GL import *
import numpy as np
from math import sin, cos, tan


# initializing glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# creating the window
window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# set window's position
glfw.set_window_pos(window, 400, 200)

# make the context current
glfw.make_context_current(window)

vertices = [-0.5, -0.5, 0.0,
             0.5, -0.5, 0.0,
             0.0,  0.5, 0.0]

colors = [1.0, 0.0, 0.0,
          0.0, 1.0, 0.0,
          0.0, 0.0, 1.0]

def window_resize(window,width,height):
    glViewport(0, 0, width, height)

glfw.set_window_size_callback(window, window_resize)

vertices = np.array(vertices, dtype=np.float32)
colors = np.array(colors, dtype=np.float32)

glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3, GL_FLOAT, 0, vertices)

glEnableClientState(GL_COLOR_ARRAY)
glColorPointer(3, GL_FLOAT, 0, colors)

#glClearColor(0, 0.1, 0.1, 1)

#glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)



# the main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.0,0.0,0.0,0.0)#PANTALLA NEGRA

    ct = glfw.get_time()  # returns the elapsed time, since init was called

    glLoadIdentity()
    #glScale(abs(sin(ct)),abs(sin(ct)),1)#glScale(abs(cos(ct)), abs(sin(ct)), 1)
    #glRotatef(tan(ct)*45,0,0,1)#glRotatef(cos(ct) * 360, 0, 0, 1)# sin 45
    #glTranslatef(sin(ct), cos(ct), 0)
    
    glScale(abs(sin(ct)),abs(sin(ct)),1)
    glRotatef((ct)*360,0,0,1)#glRotatef(tan(ct)*360,0,0,1)
    glTranslatef(sin(ct), cos(ct), 0)
    
    #glScale(abs(cos(ct)), abs(sin(ct)), 1)
    #glRotatef(cos(ct) * 360, 0, 0, 1)
    #glTranslatef(sin(ct), cos(ct), 0)

    glDrawArrays(GL_TRIANGLES, 0, 3)

    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()
