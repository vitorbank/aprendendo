from datetime import date
ano = int(input('Ano de nascimento? '))
mes = int(input('mês? '))
dia = int(input('dia? '))

def idade1(Nascimento):
    dias_no_ano = 365.2425
    idade = int((date.today() - Nascimento).days / dias_no_ano)
    return idade
print(idade1(date(ano, mes ,dia)))
1
atual = idade1(date(ano, mes, dia))
diferenca = atual - 17
if atual == 17:
    print('Vá buscar sua enxada recruta')
elif atual < 17:
    print(f'Não foi dessa vez ainda faltam {diferenca*-1} anos pra você')
else:
    print(f'Você está acima da idade de alistamento com uma diferença de {diferenca} anos')
    