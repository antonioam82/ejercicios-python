numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mifuncion(x):
    if x % 2 == 0:
        return True
    
    return False

resultado = filter(mifuncion, numeros)
print(list(resultado))
