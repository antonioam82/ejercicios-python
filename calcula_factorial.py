from VALID import ns, OKI
import subprocess

def factorial(n):
    if n == 0 or n == 1:
        resultado = 1
    elif n > 1:
        resultado = n * (factorial(n-1))
    return resultado

while True:
    num=OKI(input("Introduce número: "))
    factorial_de_n=factorial(num)
    print(factorial_de_n)

    conti=ns(input("¿Desea continuar?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
