import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

spin = 0.0

def init():
    """Inicializa la configuración de OpenGL."""
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Color de fondo: negro
    glShadeModel(GL_FLAT)

def draw_scene():
    """Dibuja la escena con un cuadrado rotado."""
    global spin
    glClear(GL_COLOR_BUFFER_BIT)  # Limpia el buffer de color
    glPushMatrix()  # Guarda la matriz actual
    glRotatef(spin, 0.0, 0.0, 1.0)  # Rotación en el eje Z
    glColor3f(1.0, 1.0, 1.0)  # Color del cuadrado: blanco
    glRectf(-25.0, -25.0, 25.0, 25.0)  # Dibuja el cuadrado
    glPopMatrix()  # Restaura la matriz guardada
    pygame.display.flip()  # Intercambia los buffers para mostrar el renderizado

def spin_display():
    """Aumenta el ángulo de rotación."""
    global spin
    spin += 2.0
    if spin > 360.0:
        spin -= 360.0

def reshape(width, height):
    """Maneja el redimensionamiento de la ventana."""
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-50.0, 50.0, -50.0, 50.0, -1.0, 1.0)  # Proyección ortogonal
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    """Función principal para configurar y ejecutar el programa."""
    pygame.init()  # Inicializa Pygame
    window_size = (250, 250)
    pygame.display.set_mode(window_size, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Rotating Square with Pygame and PyOpenGL')

    init()  # Inicializa OpenGL
    reshape(250, 250)  # Establece la vista inicial

    running = True
    spinning = False  # Controla si el cuadrado está girando o no

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:  # Salir de la ventana
                running = False
            elif event.type == KEYDOWN:
                if event.key == pygame.K_RIGHT:  # Botón izquierdo del ratón
                    spinning = True
                elif event.key == pygame.K_LEFT:  # Botón del medio del ratón
                    spinning = False

        if spinning:
            spin_display()  # Actualiza el ángulo de rotación

        draw_scene()  # Dibuja la escena
        pygame.time.wait(10)  # Espera para controlar la velocidad de rotación

    pygame.quit()  # Cierra Pygame

if __name__ == '__main__':
    main()
