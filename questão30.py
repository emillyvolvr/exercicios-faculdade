# par alto ou baixo

n = int(input("digite um número: "))

if n % 2 == 0:
    if n > 100:
        print("par alto")
    else:
        print("par baixo")
else:
    print("ímpar")