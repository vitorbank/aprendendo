def repete():
    print('Escolha o sexo: ')
f=0
m=0
while True:
    print('Escolha o sexo: ')
    escolha=input("M/F: ").lower()
    if escolha == 'f':
        print("você é mulher")
        break
    elif escolha=="m":
        print("você é homem")
        break
    else:
        print("invalido")
        repete