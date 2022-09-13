def repete():
    print(f"[{num1}]-somar\n[{num2}]-multiplicar\n[{num3}]-maior\n[{num4}]-novos\n[{num5}]-sair\n ")
n1=0
n2=0
num1=1
num2=2
num3=3
num4=4
num5=5
while True:
    print(f"[{1}]-somar\n[{2}]-multiplicar\n[{3}]-maior\n[{4}]-novos\n[{5}]-sair\n ")
    opção=int(input("qual sua opção?\n"))
    if opção==num1 or opção==num2 or opção==num3 or opção==num4==opção==num5:
        n1=int(input(f"primeiro numero: "))
        n2=int(input(f"segundo numero: "))
        if opção==num1:
            soma=n1+n2
            print(f'{n1}+{n2}={soma}')
            repete
        elif opção==num2:
            multi=n1*n2
            print(f"{n1}x{n2}={multi}")
        elif opção==num3:
            if n1>n2:
                print(f"{n1} é maior que {n2}")
                repete
            elif n1<n2:
                print(f'{n2} é maior que {n1}')
                repete
            else:
                print(f'{n1} é igual a {n2}')
                repete
        elif opção == num4:
            repete
    elif opção == num5:
        print("Saindo")
        break
    elif opção!=num1 and opção !=num2 and opção !=num3 and opção !=num4 and opção !=num5:
        print("opção invalida")
        repete