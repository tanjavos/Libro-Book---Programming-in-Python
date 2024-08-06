n=int(input("Introduce un numero entero:"))
a=n
i=0
while a//10!=0:
    a=a//10
    i=i+1
b=n
m=0
print ("i is ", i)
for j in range(i,-1,-1):
    print("j is ", j)
    d=1
    for k in range(0,j):
        print("k is ", k)
        d=d*10
    m=m+(b%10)*d
    b=b//10
print ("El resultado es: {0}".format(m))
