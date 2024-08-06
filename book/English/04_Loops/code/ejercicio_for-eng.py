a=int(input("Enter an integer number:"))
b=int(input("Enter an integer number:"))
if (a > b):
    aux=a
    a=b
    b=aux
result=1
for i in range(a+1,b+1):
    result=result*i
print("The result is:",result)