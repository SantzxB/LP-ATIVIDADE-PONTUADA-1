import os

os.system("cls||clear")



numero_A = int(input("Digite um valor que será representado pela letra A:"))
numero_B = int(input("Digite um segundo valor que serpá representado pela letra B:"))
numero_C = int(input("Digite um terceiro valor que será representado pela letra C:"))

soma = numero_A + numero_B

if soma < numero_C:
    print("A soma de A + B é menor que C. ")
else:
    print("A soma de A + B é maior que C.")
