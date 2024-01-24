import pygame
import numpy as np
import math

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("3D projection in pygame!")
screen = pygame.display.set_mode((WIDTH,HEIGHT))

points = []

points.append(np.matrix([[-1], [-1], [1]]))
points.append(np.matrix([[1], [-1], [1]]))
points.append(np.matrix([[1], [1], [1]]))
points.append(np.matrix([[-1], [1], [1]]))
points.append(np.matrix([[-1], [-1], [-1]]))
points.append(np.matrix([[1], [-1], [-1]]))
points.append(np.matrix([[1], [1], [-1]]))
points.append(np.matrix([[-1], [1], [-1]]))

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
    ])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()



screen.fill(WHITE)

for point in points:
    projected2d = np.dot(projection_matrix, point)
    pygame.draw.circle(screen, BLACK, (


pygame.display.update()
