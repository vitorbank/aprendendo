print("Bem vindo ao conversor")
formato = int(input('Escolha o formato desejado:\nbinário-1\noctal-2\nhexadecimal-3:  '))
num = int(input('Digite o numero a ser convertido:  '))
binario = bin(num)[2:]
octa = oct(num)[2:]
hexa = hex(num)[2:]
if formato == 1:
    print(f'{num} convertido em Binario é: {binario}')
elif formato == 2:
    print(f"{num} convertido em octal é: {octa}")
elif formato == 3:
    print(f"{num} convertido em hexadecimal é: {hexa}")
else:
    print("Opção invalida!")
    