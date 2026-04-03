# resto da divisão por 3 em ordem decrescente

a = int (input("digite um número: "))
b = int (input("digite um número: "))
c = int (input("digite um número:"))

r1 = a % 3
r2 = b % 3
r3 = c % 3

# ordenando manualmente (sem lista)
if r1 >= r2 and r1 >= r3:
    if r2 >= r3:
        print(r1, r2, r3)
    else:
        print(r1, r3, r2)
elif r2 >= r1 and r2 >= r3:
    if r1 >= r3:
        print(r2, r1, r3)
    else:
        print(r2, r3, r1)
else:
    if r1 >= r2:
        print(r3, r1, r2)
    else:
        print(r3, r2, r1)