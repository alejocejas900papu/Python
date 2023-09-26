import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

print("-------------------------------------------------------")
print("ADIVINANZA 1.")
print("-------------------------------------------------------")

adivinanza = " si es un animal y ladra que es "

print(adivinanza)
print("Opciones:")
print("A) Gato")
print("B) Perro")
print("C) Pájaro")

respuesta = input("Selecciona la letra de la respuesta correcta (A, B o C): ").lower()

if respuesta == "b":
    print("¡Correcto! ¡Felicitaciones!")
    print("\U0001F600","\U0001F600","\U0001F600")
else:
    print("Incorrecto. La respuesta correcta es 'B) Perro'.")
    print("\U0001F92A","\U0001F92A","\U0001F92A")