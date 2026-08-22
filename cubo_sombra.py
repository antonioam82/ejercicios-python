"""
Cubo 3D sobre una superficie con sombra proyectada (OpenGL + pygame).

Esta version usa pygame para crear la ventana en vez de GLUT, para evitar
el error "NullFunctionError: glutInit" que ocurre en Windows cuando
freeglut.dll no esta instalado.

Requisitos:
    pip install pygame PyOpenGL PyOpenGL_accelerate

Ejecutar:
    python cubo_sombra_pygame.py

Controles:
    - Flechas izquierda/derecha/arriba/abajo: mover la luz
    - T / R: girar toda la escena alrededor del eje Y
    - ESC o cerrar ventana: salir
"""

import sys
import time

import pygame
from pygame.locals import (
    DOUBLEBUF, OPENGL, QUIT, KEYDOWN,
    K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_DOWN,
    K_t, K_r, K_o, K_p
)

from OpenGL.GL import *
from OpenGL.GLU import *

# ----------------------------------------------------------------------
# Estado global
# ----------------------------------------------------------------------
angle = 0.0
scene_angle = 0.0                  # rotacion de toda la escena sobre el eje Y
light_pos = [2.0, 4.0, 2.0, 1.0]   # posicion de la luz (w=1 -> luz puntual)


# ----------------------------------------------------------------------
# Matriz de sombra (proyeccion plana desde la luz)
# ----------------------------------------------------------------------
def shadow_matrix(plane, light):
    """
    plane: (a, b, c, d) tal que a*x + b*y + c*z + d = 0
    light: (x, y, z, w)  w=1 -> luz puntual, w=0 -> luz direccional
    Devuelve una lista plana column-major lista para glMultMatrixf.
    """
    a, b, c, d = plane
    x, y, z, w = light
    dot = a * x + b * y + c * z + d * w

    m = [[0.0] * 4 for _ in range(4)]
    m[0][0] = dot - x * a; m[0][1] = -x * b;       m[0][2] = -x * c;       m[0][3] = -x * d
    m[1][0] = -y * a;      m[1][1] = dot - y * b;  m[1][2] = -y * c;       m[1][3] = -y * d
    m[2][0] = -z * a;      m[2][1] = -z * b;       m[2][2] = dot - z * c;  m[2][3] = -z * d
    m[3][0] = -w * a;      m[3][1] = -w * b;       m[3][2] = -w * c;       m[3][3] = dot - w * d

    flat = []
    for col in range(4):
        for row in range(4):
            flat.append(m[row][col])
    return flat


# ----------------------------------------------------------------------
# Geometria
# ----------------------------------------------------------------------
def draw_ground():
    size = 6
    glColor3f(0.75, 0.75, 0.78)
    glBegin(GL_QUADS)
    glVertex3f(-size, 0.0, -size)
    glVertex3f(-size, 0.0, size)
    glVertex3f(size, 0.0, size)
    glVertex3f(size, 0.0, -size)
    glEnd()

    glDisable(GL_LIGHTING)
    glColor3f(0.55, 0.55, 0.6)
    glBegin(GL_LINES)
    i = -size
    while i <= size:
        glVertex3f(i, 0.001, -size)
        glVertex3f(i, 0.001, size)
        glVertex3f(-size, 0.001, i)
        glVertex3f(size, 0.001, i)
        i += 1
    glEnd()
    glEnable(GL_LIGHTING)


def draw_cube(color=True):
    vertices = [
        (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5),
        (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5),
        (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5),
        (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5),
    ]
    faces = [
        (0, 1, 2, 3, (0, 0, -1), (0.85, 0.25, 0.25)),
        (4, 5, 6, 7, (0, 0, 1), (0.25, 0.85, 0.25)),
        (0, 4, 7, 3, (-1, 0, 0), (0.25, 0.25, 0.85)),
        (1, 5, 6, 2, (1, 0, 0), (0.9, 0.9, 0.25)),
        (3, 2, 6, 7, (0, 1, 0), (0.9, 0.9, 0.9)),
        (0, 1, 5, 4, (0, -1, 0), (0.4, 0.4, 0.4)),
    ]
    glBegin(GL_QUADS)
    for i0, i1, i2, i3, normal, col in faces:
        glNormal3f(*normal)
        if color:
            glColor3f(*col)
        for idx in (i0, i1, i2, i3):
            glVertex3f(*vertices[idx])
    glEnd()


def draw_light_marker():
    """Pequeño cubo amarillo en la posicion de la luz (sin usar GLUT)."""
    glPushMatrix()
    glDisable(GL_LIGHTING)
    glTranslatef(*light_pos[:3])
    glColor3f(1.0, 1.0, 0.4)
    s = 0.08
    glBegin(GL_QUADS)
    for dx in (-1, 1):
        glVertex3f(dx * s, -s, -s); glVertex3f(dx * s, s, -s)
        glVertex3f(dx * s, s, s);   glVertex3f(dx * s, -s, s)
    for dy in (-1, 1):
        glVertex3f(-s, dy * s, -s); glVertex3f(s, dy * s, -s)
        glVertex3f(s, dy * s, s);   glVertex3f(-s, dy * s, s)
    for dz in (-1, 1):
        glVertex3f(-s, -s, dz * s); glVertex3f(s, -s, dz * s)
        glVertex3f(s, s, dz * s);   glVertex3f(-s, s, dz * s)
    glEnd()
    glEnable(GL_LIGHTING)
    glPopMatrix()


# ----------------------------------------------------------------------
# OpenGL init / resize
# ----------------------------------------------------------------------
def init_gl(w, h):
    glClearColor(0.55, 0.7, 0.9, 1.0)
    glEnable(GL_DEPTH_TEST)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 0.95, 1.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.25, 0.25, 0.3, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glShadeModel(GL_SMOOTH)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50.0, w / float(h), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


# ----------------------------------------------------------------------
# Dibujo de un frame
# ----------------------------------------------------------------------
def render(dt):
    global angle
    angle += dt * 40.0  # grados por segundo

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(4.0, 3.5, 6.0,
              0.0, 0.5, 0.0,
              0.0, 1.0, 0.0)

    # Rotar toda la escena (suelo + cubo + sombra + luz) alrededor del eje Y.
    # Al aplicarse aqui, despues de gluLookAt, la camara permanece fija
    # y es el "mundo" el que gira delante de ella.
    glRotatef(scene_angle, 0.0, 1.0, 0.0)

    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

    # Suelo
    draw_ground()

    # Sombra proyectada
    plane = (0.0, 1.0, 0.0, 0.0)
    smat = shadow_matrix(plane, light_pos)

    glPushMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_DEPTH_TEST)
    glColor4f(0.05, 0.05, 0.05, 0.5)

    glEnable(GL_POLYGON_OFFSET_FILL)
    glPolygonOffset(-1.0, -1.0)

    glMultMatrixf(smat)
    glTranslatef(0.0, 0.5, 0.0)
    glRotatef(angle, 0.3, 1.0, 0.1)
    draw_cube(color=False)

    glDisable(GL_POLYGON_OFFSET_FILL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glPopMatrix()

    # Cubo real
    glPushMatrix()
    glTranslatef(0.0, 0.5, 0.0)
    glRotatef(angle, 0.3, 1.0, 0.1)
    draw_cube(color=True)
    glPopMatrix()

    # Marcador de luz
    draw_light_marker()


# ----------------------------------------------------------------------
# Bucle principal
# ----------------------------------------------------------------------
def main():
    global scene_angle

    pygame.init()
    width, height = 900, 700
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Cubo con sombra proyectada - OpenGL (pygame)")

    init_gl(width, height)

    clock = pygame.time.Clock()
    step = 0.06        # velocidad de movimiento de la luz
    rot_step = 60.0     # grados por segundo al girar la escena (se multiplica por dt)
    running = True

    print("Controles: flechas para mover la luz, T/R para girar la escena, ESC para salir.")

    while running:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            light_pos[0] -= step
        if keys[K_RIGHT]:
            light_pos[0] += step
        if keys[K_UP]:
            light_pos[2] -= step
        if keys[K_DOWN]:
            light_pos[2] += step
        if keys[K_o]:
            light_pos[1] -= step
        if keys[K_p]:
            light_pos[1] += step

        if keys[K_t]:
            scene_angle += rot_step * dt
        if keys[K_r]:
            scene_angle -= rot_step * dt

        render(dt)
        pygame.display.flip()

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
