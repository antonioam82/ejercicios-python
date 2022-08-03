
#CREAR FICHERO
fichero = open('miFicheroNuevo.txt', 'x')
fichero.close()

#ESCRIBIR EN FICHERO
fichero = open('miFicheroNuevo.txt', 'w')
lineas = [
    'Linea1\n',
    'Linea2\n',
    'Linea3\n',
    'Linea4\n'
    ]

fichero.writelines(lineas)
fichero.close()
