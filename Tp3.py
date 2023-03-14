#Descripcion de Trabajo
print("-------------------------------")
print("Ejercicio 3 Puntaje Final")
print("-------------------------------")
#Ingreso de datos
RC=int (input("Ingrese numero de respuestas correctas "))
RI=int (input("Ingrese numero de respuestas incorrectas "))
RB=int (input("Ingrese numero de respuestas en blaco "))
#Proceso
PCR=RC*3
PRI=RI*-1
PRB=RB*0
PF=PCR+PRI+PRB
#Solida
print ("El puntaje total es ", PF)