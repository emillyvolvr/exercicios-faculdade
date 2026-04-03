# par ou ímpar no intervalo

n = int(input("digite um número: "))

if n >= 1 and n <= 100:
    if n % 2 == 0:
        print("par no intervalo")
    else:
        print("ímpar no intervalo")
else:
    print("fora do intervalo")