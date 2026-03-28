# a) multiplicação entre dois números
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

result = n1 * n2

print("O resultado da multiplicação é", result)

# b) média 
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))
n5 = float(input("Digite o quinto número: "))

media = (n1 + n2 + n3 + n4 + n5) / 5

print("Resultado B:", media)

# c) preço com acréscimo de 8%

valor = float(input("Digite o valor do produto: "))

preco_final = valor + (valor * 0.08)

print("O preço final é", preco_final)

# d) subtração entre dois números

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

resultado = n1 - n2

print("O resultado da subtração é", resultado)

# e) cálculo do IMC

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura ** 2)

print("O IMC é", imc)

# f) conversão de temperatura

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("A temperatura em Fahrenheit é", fahrenheit)

# g) cálculo do salário

horas = float(input("Digite as horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora: "))

salario = horas * valor_hora

print("O salário total é", salario)