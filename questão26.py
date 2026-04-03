# classificação do número

n = int(input("digite um número: "))

if n > 0:
    if n < 10:
        print("pequeno")
    elif n <= 100:
        print("médio")
    else:
        print("grande")
else:
    print("negativo ou zero")