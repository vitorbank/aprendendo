for c in range(1,6):
    peso=float(input(f"peso:"))
    if c ==1:
        maior=peso
        menor=peso
    elif peso > maior:
        maior=peso
    elif peso<menor:
        menor=peso
print(f"maior peso{maior}kg menor peso {menor}kg")