a = int( input("Entre com um número inteiro: "))

if ((a % 2) == 0):
    print("Número par")
else:
    print("Número ímpar")    

print("Fim do programa")

# teste 2 utilizando "elif"
a = int(input("Entre com o primeiro número: "))
b = int(input("Entre com o segundo número: "))
c = int(input("Entre com o terceiro número: "))

if a >= b and a >= c:
    print("O maior número é o primeiro")
elif b >= a and b >= c:
    print("O maior número é o segundo")
else:
    print("O maior número é o terceiro")