print("informe os dados solicitados a seguir.")
a=float(input("Informe o valor do ponto a:  "))
b=float(input('Informe o valor do ponto b:  '))
c=float(input("informe o valor do ponto c:  "))
if a<b+c and b<c+a and c<b+a:
    if a==b and b==c:
        print(f'{a}, {b} e {c} formam um Triangulo Equilatero')
    elif a!=b!=c!=a:
        print(f'{a}, {b} e {c} formam um Triangulo Escaleno')
    else:
        print(f'{a}, {b} e {c} formam um Triangulo Isoceles')
else:
    print(f'{a}, {b} e {c} não formam um triangulo')