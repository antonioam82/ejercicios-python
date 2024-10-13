import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(5.0)
    glEnable(GL_MAP1_VERTEX_3)

def draw_curve():
    # Definir los puntos de control de la curva de Bézier
    control_points = np.array([
        [-4.0, -4.0, 0.0],
        [-2.0,  4.0, 0.0],
        [ 2.0, -4.0, 0.0],
        [ 4.0,  4.0, 0.0]
    ], dtype='float32')

    # Configurar el evaluator para la curva de Bézier de grado 3
    glMap1f(GL_MAP1_VERTEX_3, 0.0, 1.0, control_points)

    # Dibujar la curva de Bézier utilizando el evaluator
    glBegin(GL_LINE_STRIP)
    for i in range(101):
        t = i / 100.0
        glEvalCoord1f(t)  # Evaluar la curva para el valor de t
    glEnd()

    # Dibujar los puntos de control
    glColor3f(1.0, 0.0, 0.0)  # Color rojo para los puntos de control
    glBegin(GL_POINTS)
    for point in control_points:
        glVertex3fv(point)
    glEnd()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Bezier Curve using Evaluators in OpenGL')

    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    init()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)
        draw_curve()
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
