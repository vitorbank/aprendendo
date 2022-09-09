from time import sleep
import random
sleep(1.5)
print("VAMOS JOGAR UM JOGO :3")
sleep(1)
print("UM JOGO FACÍL QUE ATÉ VOCÊ ENTENDERIA")
sleep(1)
print("Jokenpô!!!")
sleep(1)
vc=input("Escolha entre pedra, papel e tesoura:  ").upper()
jogadas=["PEDRA", "PAPEL", "TESOURA"]
pc=random.choice(jogadas)
sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")
sleep(1)
if vc==pc:
    print(f"Você escolheu {vc} e eu escolhi {pc} EMPATE!!!")
elif vc== "PEDRA" and pc == "TESOURA":
    print(f"Você escolheu {vc} e eu escolhi {pc} Você Ganhou!")
elif vc=="PEDRA" and pc == "PAPEL":
    print(f"Você escolheu {vc} e eu {pc} Você perdeu!")
elif vc =="PAPEL" and pc == "PEDRA":
    print(f"Você escolheu {vc} e eu escolhi {pc} Você Ganhou!")
elif vc == 'PAPEL' and pc == "TESOURA":
    print(f"Você escolheu {vc} e eu {pc} Você perdeu!")
elif vc =="TESOURA" and pc == "PAPEL":
    print(f"Você escolheu {vc} e eu escolhi {pc} Você Ganhou!")
elif vc == "TESOURA" and pc == "PEDRA":
    print(f"Você escolheu {vc} e eu {pc} Você perdeu!")
else:
    print("Escolha um dos Três")
