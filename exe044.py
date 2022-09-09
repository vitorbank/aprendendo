normal=int(input("Valor do produto:  "))
forma=int(input("forma de pagamento:\n1  dinheiro\n2  cheque\n3  cartão   "))
if forma == 1 or forma == 2:
    print(f"o valor do produto ficaria em R${normal-(normal*0.30):.2f}")
elif forma == 3:
    parcelamento=int(input("Quantidade de parcelas:  "))
    if parcelamento<=1:
        print(f"o valor a vista no cartão é de R${normal-(normal*0.05):.2f}")
    elif parcelamento==2:
        print(f"o valor em 2x ficaria em R${normal:.2f}")
    else:
        print(f"O valor ficaria em {normal+(normal*0.20):.2f}")
else:
    print("Forma de pagamento invalida")
