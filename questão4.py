import os


os.system("cls||clear")

print("""
                Até 5kg       | Acima de 5 Kg
    Morango   |R$2,50 por Kg  | R$2,20 por Kg
    Maçã      |R$1,80 por Kg  | R$1,50 por Kg
     """)

quantidade_morango = int(input("Qual seria a quantidades de morango que você deseja?"))
quantidade_maca = int(input("Qual seria a quantidade de maçãs que você deseja:"))
soma_frutas = quantidade_maca + quantidade_morango





if quantidade_morango >= 5:
     valor = 2.20
elif quantidade_morango <= 4:
     valor = 2.50
elif quantidade_maca >= 5:
     valor = 1.50
else:       
     valor = 1.80

total_MG = quantidade_morango * valor
total_MC = quantidade_maca * valor
print(f"O valor de Maça foi: {total_MC}")
print(f"O valor do Morango foi: {total_MG}")

total_compra = total_MC + total_MG

if quantidade_maca and quantidade_morango == 10 or total_compra >= 10:
     print(" foi a aplicada uma promoção de 10%")
     valor = total_compra / 10
     print()
     print(f" o valor total com desconto ficou: {valor}")
else:
     print("Obrigado pela preferência.")
