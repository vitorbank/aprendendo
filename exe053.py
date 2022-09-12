frase = str(input("Frase:  ")).strip().lower()
palavra=frase.split()
junto="".join(palavra)
inverso=""
for letra in range (len(junto)-1,-1,-1):
    inverso+=junto[letra]
print(f"o inverso de {junto} é {inverso}")
if inverso == junto:
    print("temos um palindromo")
else:
    print("não é um palindromo")