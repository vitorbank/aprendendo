from time import sleep
print("Vamos comparar os numeros!")
sleep(0.5)
a=int(input('Digite o primeiro numero:  '))
b=int(input('Digite o segundo numero:  '))
if a>b:
    print(f"{a} é maior que {b}")
elif a<b:
    print(f"{b} é maior que {a}")
else:
    print(f"{a} e {b} são iguais")