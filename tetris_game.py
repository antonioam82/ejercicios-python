import pygame
import random

pygame.init()

# --- Configuración del tablero y la ventana ---
ANCHO_CELDA = 30
COLUMNAS = 10
FILAS = 20
ANCHO_TABLERO = COLUMNAS * ANCHO_CELDA
ALTO_TABLERO = FILAS * ANCHO_CELDA
PANEL_LATERAL = 180
ANCHO_VENTANA = ANCHO_TABLERO + PANEL_LATERAL
ALTO_VENTANA = ALTO_TABLERO

NEGRO = (10, 10, 20)
GRIS = (40, 40, 50)
BLANCO = (240, 240, 240)

COLORES = {
    'I': (0, 240, 240), 'O': (240, 240, 0), 'T': (160, 0, 240),
    'S': (0, 240, 0),   'Z': (240, 0, 0),   'J': (0, 0, 240),
    'L': (240, 160, 0),
}

# --- Definición de las siete piezas y sus rotaciones ---
FORMAS = {
    'I': [[(0,0),(1,0),(2,0),(3,0)], [(0,0),(0,1),(0,2),(0,3)]],
    'O': [[(0,0),(1,0),(0,1),(1,1)]],
    'T': [[(0,0),(1,0),(2,0),(1,1)], [(1,0),(0,1),(1,1),(1,2)],
          [(1,0),(0,1),(1,1),(2,1)], [(0,0),(0,1),(1,1),(0,2)]],
    'S': [[(1,0),(2,0),(0,1),(1,1)], [(0,0),(0,1),(1,1),(1,2)]],
    'Z': [[(0,0),(1,0),(1,1),(2,1)], [(1,0),(0,1),(1,1),(0,2)]],
    'J': [[(0,0),(0,1),(1,1),(2,1)], [(0,0),(1,0),(0,1),(0,2)],
          [(0,0),(1,0),(2,0),(2,1)], [(1,0),(1,1),(0,2),(1,2)]],
    'L': [[(2,0),(0,1),(1,1),(2,1)], [(0,0),(0,1),(0,2),(1,2)],
          [(0,0),(1,0),(2,0),(0,1)], [(0,0),(1,0),(1,1),(1,2)]],
}


class Pieza:
    def __init__(self, tipo):
        self.tipo = tipo
        self.rotacion = 0
        self.x = COLUMNAS // 2 - 2   # aparece centrada arriba
        self.y = 0

    def celdas(self):
        forma = FORMAS[self.tipo][self.rotacion % len(FORMAS[self.tipo])]
        return [(self.x + cx, self.y + cy) for cx, cy in forma]

    def rotar(self):
        self.rotacion = (self.rotacion + 1) % len(FORMAS[self.tipo])


def crear_tablero():
    return [[None for _ in range(COLUMNAS)] for _ in range(FILAS)]


def colision(tablero, pieza, dx=0, dy=0, rotacion=None):
    rot_original = pieza.rotacion
    if rotacion is not None:
        pieza.rotacion = rotacion
    for x, y in pieza.celdas():
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= COLUMNAS or ny >= FILAS:
            pieza.rotacion = rot_original
            return True
        if ny >= 0 and tablero[ny][nx] is not None:
            pieza.rotacion = rot_original
            return True
    pieza.rotacion = rot_original
    return False


def fijar_pieza(tablero, pieza):
    for x, y in pieza.celdas():
        if y >= 0:
            tablero[y][x] = pieza.tipo


def limpiar_lineas(tablero):
    nuevas = [fila for fila in tablero if any(c is None for c in fila)]
    lineas_completas = FILAS - len(nuevas)
    for _ in range(lineas_completas):
        nuevas.insert(0, [None for _ in range(COLUMNAS)])
    return nuevas, lineas_completas


def nueva_pieza():
    return Pieza(random.choice(list(FORMAS.keys())))


def dibujar_tablero(pantalla, tablero):
    for y in range(FILAS):
        for x in range(COLUMNAS):
            rect = (x * ANCHO_CELDA, y * ANCHO_CELDA, ANCHO_CELDA, ANCHO_CELDA)
            if tablero[y][x] is not None:
                pygame.draw.rect(pantalla, COLORES[tablero[y][x]], rect)
            pygame.draw.rect(pantalla, GRIS, rect, 1)


def dibujar_pieza(pantalla, pieza):
    color = COLORES[pieza.tipo]
    for x, y in pieza.celdas():
        if y >= 0:
            rect = (x * ANCHO_CELDA, y * ANCHO_CELDA, ANCHO_CELDA, ANCHO_CELDA)
            pygame.draw.rect(pantalla, color, rect)
            pygame.draw.rect(pantalla, NEGRO, rect, 1)


def main():
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Tetris en Python")
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("Arial", 22)

    tablero = crear_tablero()
    pieza_actual = nueva_pieza()
    siguiente_pieza = nueva_pieza()
    puntuacion = 0
    game_over = False

    tiempo_caida = 0
    velocidad_caida = 500  # ms entre caídas automáticas; baja este valor para más dificultad

    while not game_over:
        dt = reloj.tick(60)
        tiempo_caida += dt

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and not colision(tablero, pieza_actual, dx=-1):
                    pieza_actual.x -= 1
                elif evento.key == pygame.K_RIGHT and not colision(tablero, pieza_actual, dx=1):
                    pieza_actual.x += 1
                elif evento.key == pygame.K_DOWN and not colision(tablero, pieza_actual, dy=1):
                    pieza_actual.y += 1
                elif evento.key == pygame.K_UP:
                    nueva_rotacion = (pieza_actual.rotacion + 1) % len(FORMAS[pieza_actual.tipo])
                    if not colision(tablero, pieza_actual, rotacion=nueva_rotacion):
                        pieza_actual.rotacion = nueva_rotacion
                elif evento.key == pygame.K_SPACE:
                    while not colision(tablero, pieza_actual, dy=1):
                        pieza_actual.y += 1

        if tiempo_caida >= velocidad_caida:
            tiempo_caida = 0
            if not colision(tablero, pieza_actual, dy=1):
                pieza_actual.y += 1
            else:
                fijar_pieza(tablero, pieza_actual)
                tablero, lineas = limpiar_lineas(tablero)
                velocidad_caida -= 5
                puntuacion += lineas * 100
                pieza_actual = siguiente_pieza
                siguiente_pieza = nueva_pieza()
                if colision(tablero, pieza_actual):
                    game_over = True

        pantalla.fill(NEGRO)
        dibujar_tablero(pantalla, tablero)
        dibujar_pieza(pantalla, pieza_actual)

        texto_puntos = fuente.render(f"Puntos: {puntuacion}", True, BLANCO)
        pantalla.blit(texto_puntos, (ANCHO_TABLERO + 20, 20))
        texto_siguiente = fuente.render("Siguiente:", True, BLANCO)
        pantalla.blit(texto_siguiente, (ANCHO_TABLERO + 20, 70))
        for x, y in siguiente_pieza.celdas():
            rect = (ANCHO_TABLERO + 30 + x * 20, 110 + y * 20, 20, 20)
            pygame.draw.rect(pantalla, COLORES[siguiente_pieza.tipo], rect)

        if game_over:
            texto_fin = fuente.render("GAME OVER", True, (255, 60, 60))
            pantalla.blit(texto_fin, (ANCHO_TABLERO + 20, 200))

        pygame.display.flip()

    pygame.time.wait(2000)
    pygame.quit()


if __name__ == "__main__":
    main()
