mulhernova=0
homivei=0
nomevei=""
somaidade=0
mediaidade=0
for c in range (1,5):
    print(f"------{c}ª pessoa------")
    nome=input("nome: ")
    idade=int(input("idade: "))
    sexo=str(input("sexo: ")).strip()
    somaidade+=idade
    if c ==1 and sexo in"Hh":
        homivei=idade
        nomevei=nome
    if sexo in"Hh" and idade >homivei:
        homivei=idade
        nomevei=nome
    if sexo in'Mm' and idade <20:
        mulhernova+=1
mediaidade=somaidade/4
print(f"A Media de idades é de {mediaidade} anos ")
print(f"o vei mais vei é o {nomevei} com {homivei} anos")
print (f"o grupo tem {mulhernova} mulher com menos de 20 anos")