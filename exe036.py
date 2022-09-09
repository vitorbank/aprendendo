import math
print('Bem-vindo ao nosso banco')
print('Escolha a opção desejada:')
opcao = int(input('\n1 Emprestimo\n2 pagar boleto '))
if opcao == 1:
    valor= int(input('Informe o valor desejado: '))
    salario= int(input('informe seu salario: '))
    tempo = int(input('Em quantos anos deseja pagar? '))
    if valor/(tempo*12) >= salario*0.30:
        print("Lamentamos informar que a\n parcela seria maior que 30% de seu salario")
        print(f"Quantidade de parcelas{tempo*12} \nvalor de parcelas{valor/(tempo*12)}")
    else:
        print("Parabéns emprestimo aprovado")
        print(f"Quantidade de parcelas{tempo*12} \nvalor de parcelas{valor/(tempo*12)}") 
if opcao == 2:
    print('Operação indisponivel no momento')
if opcao != 1 or 2:
    print('Opção invalida tente novamente')
    
