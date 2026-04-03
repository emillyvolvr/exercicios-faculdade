# classificação do número

n = int(input("digite um número: "))

if n == 0:
    print("neutro")
elif n > 0 and n % 2 == 0:
    print("par positivo")
elif n > 0 and n % 2 != 0:
    print("ímpar positivo")
elif n < 0 and n % 2 == 0:
    print("par negativo")
else:
    print("ímpar negativo")