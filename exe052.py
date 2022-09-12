n1 = int(input('digite um numero para saber se ele é primo:'))
c = 0
for i in range(1, n1+1):
    if n1%i==0:
        print('\033[1;34m',end=" ")
        c+=1
    else:
        print('\033[1;33m',end=" ")
    print(f'{i}',end=" ")
print(f"\n\033[0;0m o numero {n1} foi divisivel {c} vezes")
if c == 2:
    print('Ele é primo')
else:
    print('Ele não é primo')
