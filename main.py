c=1
par=impar=0
while c !=0:
    c=int(input("Digite um valor: "))
    if c !=0:
        if c % 2 ==0:
            par +=1
        else:
            impar+=1
print(f"Você digitou {par} numeros pares e {impar} impares")