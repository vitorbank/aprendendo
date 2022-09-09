print('Bem vindo ao sistema da escola')
print('Insira as notas conforme solicitado')
a=float(input('Matemática:  '))
b=float(input('Artes:  '))
media= (a+b)/2
if media<5:
    print(f'Sua media foi {media} Você foi reprovado')
elif media>=5 and media <7:
    print(f'Sua media foi {media} Você vai para recuperação')
elif media >=7:
    print(f'Sua media foi {media} Você foi aprovado')
else:
    print('Informação ou formato invalidos')
    