cores = {'limpa': '\033[m',
         'lazul': '\033[34m',
         'lvermelho': '\033[31m',
         'lbranco': '\033[97m',
         'lamarelo': '\033[33m',
         'lverde': '\033[32m',
         'lpreto': '\033[30m',
         'lmagenta': '\033[35m',
         'lciano': '\033[36m',
         'cinza': '\033[37m',
         'fpreto': '\033[40m',
         'fvermelho': '\033[41m',
         'fverde': '\033[42m',
         'famarelo': '\033[43m',
         'fazul': '\033[44m',
         'fmagenta': '\033[45m',
         'fciano': '\033[46m',
         'fcinza': '\033[47m',
         'fbranco': '\033[107m'}
from time import sleep
print("{}Bem vindo ao BNDS! por favor \nPreencha os campos solicitados a seguir {}".format(cores['lazul'], cores['limpa']))
valor = float(input('{}Qual o valor do imovel? {}'.format(cores['lverde'], cores['limpa'])))
salario = float(input('{}Qual o valor do seu salario? {}'.format(cores['lverde'], cores['limpa'])))
tempo = int(input('{}Tempo de Parcelamento?(anos){} '.format(cores['lverde'], cores['limpa'])))
parcela = valor/(tempo*12)
dias = 1
print('{}CARREGANDO{}'.format(cores['lvermelho'],cores['limpa']))
sleep(3)
if parcela >= 0.30*salario:
    print('{}Sentimos muito, mas seu emprestimo foi negado{}'.format(cores['lvermelho'], cores['limpa']))
elif parcela <= 0.30*salario:
    print('{}Parabéns seu emprestimo for aprovado{}'.format(cores['lazul'], cores['limpa']))
print('valor do emprestimo: {:.2f}\nquantidade de parcelas: {:.2f}\nvalor das parcelas: {:.2f}\n anos: {:.2f}'.format(valor, tempo*12, parcela, tempo))
