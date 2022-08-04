from functools import reduce

def suma(a, b):
    print(f'a={a}, b={b}')
    return a + b

res = reduce(suma, [1, 2, 3, 4, 5])
print(res)
