# classificação ímpar/par e sinal

n = int(input("digite um número: "))

if n % 2 == 0 and n > 0:
    print("par positivo")
elif n % 2 == 0 and n < 0:
    print("par negativo")
else:
    print("ímpar")