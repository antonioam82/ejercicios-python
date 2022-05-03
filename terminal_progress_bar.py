import math
from colorama import Back, init

#INICIAR 'colorama'
init()

print("CALCULANDO FACTORIALES...")
def progress_bar(progress, total):
    percent = 100 * (progress / float(total))#CALCULA PORCENTAJE
    bar = (Back.GREEN+' '+Back.RESET) * int(percent) + '-' * (100 - int(percent))#DEFINE BARRA
    print(f"\r|{bar}| {percent:.2f}%", end="\r")#MUESTRA BARRA + PORCENTAJE

#GENERAR LISTA DE VALORES
numbers = [x * 5 for x in range(2000,3000)]

#RESULTADOS
results = []

#REALIZAR CALCULOS.
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))#LLAMADA A FUNCIÓN 'progress_bar()'
