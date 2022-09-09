from datetime import date
print("Bem-vindo a federação nacional de natação!")
print('Informe os dados requisitados para que seja feita sua classificação')
ano=int(input('Insira seu ano de nascimento:  '))
idade = date.today().year-ano
if idade <= 9:
    categoria="Mirim"
elif idade > 9 and idade <=14:
    categoria="Infantil"
elif idade > 14 and idade <= 19:
    categoria="Junior"
elif idade > 19 and idade <=20:
    categoria="Senior"
elif idade > 20:
    categoria="Master"
else:
    print('Informação invalida')
print(f"sua idade é {idade} e sua categoria é {categoria}")