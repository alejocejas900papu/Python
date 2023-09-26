import os
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clear()
# Finalizacion de la Limpieza de Pantalla

print("-------------------------------------------------------")
print("ADIVINANZA 1.")
print("-------------------------------------------------------")

adivinanza = "que es si es un animal y ladra"


print(adivinanza)
respuesta = input("Adivina la respuesta: ").lower()

if respuesta == "perro":
    print("¡Correcto! ¡Felicitaciones!")
    print("\U0001F600","\U0001F600","\U0001F600")
else:
    print("Incorrecto. La respuesta es 'pera'.")
    print("\U0001F92A","\U0001F92A","\U0001F92A")