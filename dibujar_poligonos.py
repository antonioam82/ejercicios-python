import pygame, sys
from pygame.locals import *

#CREAMOS VENTANA.
pygame.init()
DISPLAYGAME=pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption("Dibujando figuras")

#DEFINIMOS LOS COLORES QUE VAMOS A EMPLEAR.
negro=(0,0,0)
blanco=(255,255,255)
rojo=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)

#ESCOJEMOS EL COLOR DEL FONDO
DISPLAYGAME.fill(blanco)

#DIBUJAMOS POLIGONO.
pygame.draw.polygon(DISPLAYGAME, verde, ((146,0),(291,106),(236,277),
                                         (26,277),(0,106)))
#DIBUJAMOS LINEA.
pygame.draw.line(DISPLAYGAME, azul, (120,60), (60,120))
#DIBUJAMOS LINEA ESPECIFICANDO GROSOR.
pygame.draw.line(DISPLAYGAME, azul, (60,60), (120,60), 20)
#DIBUJAMOS CIRCULO.
pygame.draw.circle(DISPLAYGAME, rojo, (300,50),20,0)
#DIBUJAMOS ELIPSE.
pygame.draw.ellipse(DISPLAYGAME, azul, (300,250,40,80), 1)
#DIBUJAMOS RECTANGULO.
pygame.draw.rect(DISPLAYGAME, rojo, (200, 150, 100, 50))

#GENERAMOS CICLO PARA LA VENTANA.
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
