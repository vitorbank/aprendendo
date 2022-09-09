print("informe os dados solicitados a seguir.")
a=int(input("Informe o valor do ponto a:  "))
b=int(int(input('Informe o valor do ponto b:  ')))
c=int(input("informe o valor do ponto c:  "))
if a<b+c and b<c+a and c<b+a:
    if a==b and b==c:
        print(f'{a}, {b} e {c} formam um Triangulo Equilatero')
    elif a==b!=c or b==c!=a:
        print(f'{a}, {b} e {c} formam um Triangulo Isoceles')
    elif a!=b!=c:
        print(f'{a}, {b} e {c} formam um Triangulo Escaleno')
    else:
        print(f'{a},{b} e {c} não formam um triangulo')
elif a ==" " or b ==" " or c ==" ":
    print('Valor não informado')
else:
    print(f'{a}, {b} e {c} não formam um triangulo')
