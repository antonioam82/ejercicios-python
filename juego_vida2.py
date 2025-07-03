import pygame
import numpy as np

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screen.fill(bg)


nxC, nyC = 25, 25

dimCW = width / nxC
dimCH = height / nyC

# Bucle principal con control de eventos
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for y in range(0, nxC):
        for x in range(0, nyC):

            poly = [((x)  * dimCW,  y * dimCH),
                    ((x+1)* dimCW,  y * dimCH),
                    ((x+1)* dimCW, (y+1) * dimCH),
                    ((x)  * dimCW, (y+1) * dimCH)]
            pygame.draw.polygon(screen, (128, 128, 128), poly, width = 1)

    pygame.display.flip()  # Mostrar la pantalla inicial


pygame.quit()
