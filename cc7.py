print("-------------------------------------------------------")
print("Complementario 7")
print("-------------------------------------------------------")

print("Ingrese valores de la ecuación cuadrática:")
a = int( input("a: "))
b = int( input("b: "))
c = int( input("c: "))
print("-------------------------------------------------------")

d = b**2 - 4*a*c
if d > 0 :
    x1 = ( (-b) + d**0.5 )/ 2*a
    x2 = ( (-b) - d**0.5 )/ 2*a
    print("Raíces reales:", x1, x2)
else:
    print("Raíces Irracionales")