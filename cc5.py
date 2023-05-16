print("-------------------------------------------------------")
print("Complementario 5")
print("-------------------------------------------------------")

s=0

print("ingrese numero de terminos:")

n= int(input())

for x in range(1,n+1) :
    if x%2 ==0 :
        s= s - (1/x)
    else:
        s=s + (1/x)


print ("------------------------------------------------------")
print("la suma sera ", s)        
