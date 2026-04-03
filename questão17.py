# classificação por idade

idade = int(input("digite a idade: "))

if idade < 18:
    print("menor de idade")
elif idade <= 59:
    print("adulto")
else:
    print("idoso")