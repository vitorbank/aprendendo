soma=0
cont=0
for c in range(1,7):
    n=int(input("Insira um numero inteiro: "))
    if n%2==0:
        soma+=n
        cont=cont+1
    if n%2!=0:
        print("somente numeros pares")
print(f"{cont} numeros  com soma de {soma}")