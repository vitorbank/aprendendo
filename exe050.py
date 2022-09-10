soma=0
for c in range(1,6):
    n=int(input("Insira um numero inteiro: "))
    if n%2==0:
        soma+=n
        print(soma)
    if n%2!=0:
        print("somente numeros pares")