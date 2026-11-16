import random

PALABRAS = ["python", "programa", "variable", "funcion", "bucle", "lista", "archivo"]
MAX_FALLOS = 6


def dibujar(fallos):
    """Devuelve el dibujo del ahorcado según el número de fallos."""
    cabeza = "O" if fallos >= 1 else " "
    torso = "|" if fallos >= 2 else " "
    brazo_izq = "/" if fallos >= 3 else " "
    brazo_der = "\\" if fallos >= 4 else " "
    pierna_izq = "/" if fallos >= 5 else " "
    pierna_der = "\\" if fallos >= 6 else " "

    return f"""
  +---+
  |   |
  {cabeza}   |
 {brazo_izq}{torso}{brazo_der}  |
 {pierna_izq} {pierna_der}  |
      |
========="""


def mostrar_palabra(palabra, acertadas):
    return " ".join(letra if letra in acertadas else "_" for letra in palabra)


def jugar():
    palabra = random.choice(PALABRAS)
    acertadas = set()
    falladas = set()

    while len(falladas) < MAX_FALLOS:
        print(dibujar(len(falladas)))
        print("\n" + mostrar_palabra(palabra, acertadas))
        print(f"Intentos restantes: {MAX_FALLOS - len(falladas)} | Falladas: {' '.join(sorted(falladas))}")

        letra = input("Elige una letra: ").lower().strip()

        if len(letra) != 1 or not letra.isalpha():
            print("Escribe una sola letra.")
            continue
        if letra in acertadas or letra in falladas:
            print("Esa letra ya la has usado.")
            continue

        if letra in palabra:
            acertadas.add(letra)
            if all(l in acertadas for l in palabra):
                print(f"\n¡Has ganado! La palabra era: {palabra}")
                return
        else:
            falladas.add(letra)

    print(dibujar(MAX_FALLOS))
    print(f"\nHas perdido. La palabra era: {palabra}")


if __name__ == "__main__":
    jugar()
