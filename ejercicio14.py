import math
from re import T
print ("-------------------------------")
print ("Ejercicio Condicioneal nuemero 14 ")
print ("-------------------------------")

print("Ingrese valores: ")
num = int( input("Tipo de Calculo: "))
v= int( input("Ingrese V: "))

print("---------------------------------")
print("ingresa que tipo de calculo queres ")
print(" (.1) 100*v ")
print(" (.2) 100**v ")
print(" (.3) 100/v ")
print("----------------------------------")

eleccion=int(input())

if(eleccion==1){
    VAL=100*v 

}
if(eleccion==2){
    VAL=100**v
}
if(eleccion==3){
    VAL=100/v
}
if(eleccion==0){
    print("error")
}
if(eleccion>=4){
    print(" es igual a 0")
}

print (VAL)
