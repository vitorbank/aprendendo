n=int(input("Numero a ser fatorado: "))
fat=1
i=2
while i<=n:
    fat=fat*i
    i=i+1
print(f'valor de {n}! é igual a {fat}')