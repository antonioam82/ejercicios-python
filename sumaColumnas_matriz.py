#SUMA DE LAS COLUMNAS DE UNA MATRIZ.
mat = [[5,7,8],[5,8,1],[7,8,0]]

for x in range(0,3):
    sumaColumn = 0
    for y in range(0,3):
        sumaColumn = sumaColumn+mat[y][x]
    print("\nSuma de la columna "+str(x+1)+": "+str(sumaColumn))
