s = 0
t=0
for c in range(1,501):
    if c%2!=0 and c%3==0:
        s+=c
        t+=1
        print(c)
print(f"a soma é: {s} e os valores são: {t}")