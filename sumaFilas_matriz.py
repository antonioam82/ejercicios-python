#SUMA FILAS DE UNA MATRIZ
mat = [[5,7,8],[5,8,1],[7,8,0]]

for x in range(0,3):
    sumaFilas = 0

    for y in range(0,3):
        sumaFilas = sumaFilas + mat[x][y]
    print("\nSuma de la fila "+str(x+1)+": "+str(sumaFilas))
    
