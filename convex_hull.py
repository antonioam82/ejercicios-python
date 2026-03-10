import random
import math
import matplotlib.pyplot as plt

# Fijamos una semilla para que la generación de puntos sea reproducible
random.seed(42)

def generar_puntos(n, rango=100):
    # Genera n puntos aleatorios dentro de un cuadrado de tamaño rango x rango
    puntos = []
    for _ in range(n):
        x = random.uniform(0, rango)
        y = random.uniform(0, rango)
        puntos.append((x, y))
    return puntos

def orientacion(p, q, r):
    # Calcula el producto cruzado de los vectores pq y pr
    # Sirve para determinar si los tres puntos forman un giro horario o antihorario
    return (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])

def angulo(p0, p1):
    # Calcula el ángulo polar entre el punto base p0 y el punto p1
    return math.atan2(p1[1]-p0[1], p1[0]-p0[0])

def convex_hull(puntos):

    # 1. Encontramos el punto con menor coordenada y (y menor x en caso de empate)
    punto_base = min(puntos, key=lambda p: (p[1], p[0]))

    # 2. Ordenamos los puntos según el ángulo polar respecto al punto base
    puntos_ordenados = sorted(puntos, key=lambda p: angulo(punto_base, p))

    # Lista donde iremos construyendo la envolvente convexa
    hull = []

    # 3. Recorremos los puntos ordenados
    for p in puntos_ordenados:

        # Mientras los tres últimos puntos formen un giro horario,
        # eliminamos el punto intermedio porque genera una concavidad
        while len(hull) >= 2 and orientacion(hull[-2], hull[-1], p) <= 0:
            hull.pop()

        # Añadimos el punto actual al hull
        hull.append(p)

    return hull


# Generar conjunto de puntos
puntos = generar_puntos(30)

# Calcular la envolvente convexa
hull = convex_hull(puntos)


# Separar coordenadas de los puntos originales
x = [p[0] for p in puntos]
y = [p[1] for p in puntos]

# Coordenadas de los puntos del hull
# Añadimos el primer punto al final para cerrar el polígono
hx = [p[0] for p in hull] + [hull[0][0]]
hy = [p[1] for p in hull] + [hull[0][1]]


# Representación gráfica
plt.scatter(x, y)      # puntos originales
plt.plot(hx, hy)       # contorno de la envolvente convexa

plt.title("Convex Hull del conjunto de puntos")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
