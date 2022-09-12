a=int(input("primeiro numero:  "))
b=int(input("Razão:  "))
c=int(input("Quantos Números:  "))
ultimo=a+(c-1)*b
ultimo=ultimo+1
for var in range(a,ultimo,b):
    print(f'{var}',end=' > ')