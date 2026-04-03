# múltiplo de 2 ou 3

n = int(input("digite um número: "))

if n > 0:
    if n % 2 == 0 and n % 3 == 0:
        print("múltiplo de 2 e 3")
    else:
        print("não atende")
else:
    print("número inválido")