# verificar múltiplo de 5

n = int(input("digite um número: "))

if n % 5 == 0:
    if n > 50:
        print("múltiplo alto")
    else:
        print("múltiplo baixo")
else:
    print("não é múltiplo")