a=int(input("Introduce un número entero:"))
b=int(input("Introduce otro número entero:"))
if (a > b):
    aux=a
    a=b
    b=aux
resultado=1
for i in range(a+1,b+1):
    resultado=resultado*i
print("El resultado es:",resultado)