import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])

    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0,-5)

    glRotatef(0, 0, 0, 0)

    x=1
    y=1
    z=1
    m=2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x=0
                    y=1
                    z=0
                if event.key == pygame.K_RIGHT:
                    x=1
                    y=0
                    z=0
                if event.key == pygame.K_UP:
                    x=0
                    y=0
                    z=1
                if event.key == pygame.K_DOWN:
                    x=1
                    y=1
                    z=1
                if event.key == pygame.K_v:
                    m+=1
                if event.key == pygame.K_b:
                    m-=1
                    
        glRotatef(m, x, y, z)#(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
