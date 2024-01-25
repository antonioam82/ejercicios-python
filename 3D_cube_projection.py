import pygame
import numpy as np
from math import *

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("3D projection in pygame!")
screen = pygame.display.set_mode((WIDTH,HEIGHT))

scale = 100

circle_pos = [WIDTH/2, HEIGHT/2]

angle = 0

points = []

points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1, 1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
    ])

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    rotation_z = np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0,0,1],
        ])

    rotation_x = np.matrix([
        [1,0,0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]
        ])

    
    rotation_y = np.matrix([
        [cos(angle), 0, sin(angle)],
        [0,1,0],
        [-sin(angle), 0, cos(angle)]
        ])    

    angle += 0.1

    screen.fill(WHITE)

    for point in points:
        #trot = np.dot(rotation_z,rotation_x,rotation_y)
        rotated2d = np.dot(rotation_y, point.reshape((3,1)))
        projected2d = np.dot(projection_matrix, rotated2d)
        x = int(projected2d[0,0] * scale) + circle_pos[0]
        y = int(projected2d[1,0] * scale) + circle_pos[1]
        pygame.draw.circle(screen, BLACK, (x, y), 5)

    pygame.display.update()
