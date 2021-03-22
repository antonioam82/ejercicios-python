import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def verts():
    global verticies
    verticies = [
    [1, -1, -1],#det inf der
    [1, 1, -1],#det sup der
    [-1, 1, -1],#det sup iz
    [-1, -1, -1],#det inf iz
    [1, -1, 1],#del inf der
    [1, 1, 1],#del sup der
    [-1, -1, 1],#del inf der
    [-1, 1, 1]#del sup iz
    ]

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

'''def change_verts1(s):
    #global vertices
    if s == 'r':
        for i in range(0,4):
            verticies[i][2] +=0.9
        for i in range(4,8):
            verticies[i][2] -= 0.09       
    else:
        for i in range(0,4):
            verticies[i][2] -=0.9
        for i in range(4,8):
            verticies[i][2] += 0.09'''

def main():
    global verticies
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    
    verts()

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)#45 0.1 50.0

    glTranslatef(0.0,0.0,-5)

    #glRotatef(0, 0, 0, 0)

    x=0
    y=0
    z=0
    m=0
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
                if event.key == pygame.K_UP:
                    x=1
                    y=0
                    z=0
                if event.key == pygame.K_RIGHT:
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
                if event.key == pygame.K_s:
                    m=0
                if event.key == pygame.K_c:
                    verts()

                if event.key == pygame.K_r:
                    verticies[0][0] += 0.09
                    verticies[1][0] += 0.09
                    verticies[4][0] += 0.09
                    verticies[5][0] += 0.09
                if event.key == pygame.K_i:
                    verticies[0][0] -= 0.09
                    verticies[1][0] -= 0.09
                    verticies[4][0] -= 0.09
                    verticies[5][0] -= 0.09
                if event.key == pygame.K_q:
                    verticies[0][2] += 0.09
                    verticies[1][2] += 0.09
                    verticies[2][2] += 0.09
                    verticies[3][2] += 0.09                    
                if event.key == pygame.K_e:
                    verticies[0][2] -= 0.09
                    verticies[1][2] -= 0.09
                    verticies[2][2] -= 0.09
                    verticies[3][2] -= 0.09
                if event.key == pygame.K_t:
                    verticies[1][1] += 0.09
                    verticies[2][1] += 0.09
                    verticies[5][1] += 0.09
                    verticies[7][1] += 0.09
                if event.key == pygame.K_y:
                    verticies[1][1] -= 0.09
                    verticies[2][1] -= 0.09
                    verticies[5][1] -= 0.09
                    verticies[7][1] -= 0.09
                    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            glRotatef(1, 1, 1, 1)
        
        glRotatef(m, x, y, z)#(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()

