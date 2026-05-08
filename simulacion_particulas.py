import pygame
import random

# Inicialización de pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

# Crear ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulación de Partículas en Python")

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Lista de partículas
particles = []

# Crear partículas iniciales
for _ in range(200):

    # Posición aleatoria
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)

    # Velocidad aleatoria
    vx = random.uniform(-2, 2)
    vy = random.uniform(-2, 2)

    # Guardar partícula
    particles.append([x, y, vx, vy])

# Variable principal del loop
running = True

# Bucle principal
while running:

    # Limpiar pantalla
    screen.fill((0, 0, 0))

    # Eventos
    for event in pygame.event.get():

        # Cerrar ventana
        if event.type == pygame.QUIT:
            running = False

    # Actualizar partículas
    for p in particles:

        # Actualizar posición
        p[0] += p[2]
        p[1] += p[3]

        # Rebote horizontal
        if p[0] < 0 or p[0] > WIDTH:
            p[2] *= -1

        # Rebote vertical
        if p[1] < 0 or p[1] > HEIGHT:
            p[3] *= -1

        # Dibujar partícula
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(p[0]), int(p[1])),
            3
        )

    # Actualizar pantalla
    pygame.display.flip()

    # Limitar FPS
    clock.tick(60)

# Salir de pygame
pygame.quit()
