#Descripcion de Trabajo
import math
print("-------------------------------")
print("Ejercicio 10")
print("-------------------------------")
#Constante
PI=3.1416
#Ingreso de datos
RADIO=int (input("Ingrese el radio del cilindro "))
ALTO=int (input("Ingrese el altura del cilindro "))
#Proceso
VOL=PI*RADIO**2*ALTO
ARE=2*PI*RADIO*(ALTO+RADIO)
#Solida
print ("El Volumen es ", VOL)
print ("El Area es ", ARE)