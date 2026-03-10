import os

os.system("cls||clear")

litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

if tipo == "A":
    preco = 3.79
    if litros <= 25:
        desconto = 0.02
    else:
        desconto = 0.04

elif tipo == "G":
    preco = 6.59
    if litros <= 25:
        desconto = 0.03
    else:
        desconto = 0.05

valor_bruto = litros * preco
valor_desconto = valor_bruto * desconto
valor_final = valor_bruto - valor_desconto

print("Valor a pagar: R$", round(valor_final, 2))
