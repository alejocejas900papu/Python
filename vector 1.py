print("-------------------------------------------------------")
print("Vector1: LECTURA DE N ELEMENTOS ENTEROS.")
print("-------------------------------------------------------")

i = 1
F = []

print("Ingrese Número de elementos a Ingresar: ")
numElementos = int( input())

while i <= numElementos:
elemento = int( input("Ingrese Elemento: "))
F.append(elemento)

print("-------------------------------------------------------")
print(F)