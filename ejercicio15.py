import math
from re import T
print ("-------------------------------")
print ("Ejercicio Condicioneal nuemero 15 ")
print ("-------------------------------")

num=int(input("iingrese un numero"))

par_Impar = {
1 : 'Impar',
3 : 'Impar',
5 : 'Impar',
7 : 'Impar',
9 : 'Impar',
2 : 'Par',
4 : 'Par',
6 : 'Par',
8 : 'Par',
10 : 'Par',

print("-------------------------------------------------------")
print(par_Impar.get(num, "Numero fuera de Rango"))