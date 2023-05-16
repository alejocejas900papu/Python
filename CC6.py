print("-------------------------------------------------------")
print("Complementario 6")
print("-------------------------------------------------------")
#Constante
aux = 0
aux2 = 0
n = int( input("Ingrese un número: "))
#Proceso
i=10
while i<=n:
    aux = n%10
    n = n // 10
    aux2 = aux2*10 + aux
aux2 = aux2*10 + n
#Salida
print("El número invertido será:", aux2)