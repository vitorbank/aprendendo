from datetime import date
t=0
p=0
for c in range(1,8):
    data=int(input('Ano de nascimento: '))
    idade=date.today().year-data
    if idade>=21:
        t=t+1
    elif idade<21:
        p=p+1
print (f'menores {p}')
print (f'maiores {t}')