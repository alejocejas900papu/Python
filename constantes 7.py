import math
from re import T
print ("-------------------------------")
print ("Ejercicio Condicioneal nuemero 7 ")
print ("-------------------------------")


PI = 3.1416 

print ( "ingrese los lados del triangulo") 
b=float ( "ingresa el lado b" ) 
c=float ("ingresa el lado c")


print("Ingrese el ángulo en grados sexagesimales:")
 alfa = float( input()) 

a = ( b**2 + c**2 - 2*b*c * math.cos( alfa*PI/180 ) )**0.50 

print ("----------------------------------------")
print ("el lado a es igual a ", a )

