from random import choice
from time import sleep
n=0
tot=0
s=[0,1,2,3,4,5,6,7,8,9,10]
c=choice(s)
while n!=c:
    n=int(input("Escolha um numero: "))
    if n!=c:
        sleep(1)
        print("Errado, tente outra vez")
sleep(1)
print(f"Acertou eu escolhi {c} e você {n}")