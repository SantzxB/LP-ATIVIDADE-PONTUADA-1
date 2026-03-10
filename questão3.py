import os


os.system("cls||clear")


n1 = int(input("Digite um valor que será representado por A:"))
n2 = int(input("Digite outro valorque será representado por B:"))


soma = n1 + n2 
multiplicacao = n1 * n2

if n1 == n2:
    print(f"A + B = {soma}")
    print()
    print("A soma dos dois valores será representada pela letra C")
else:
    print(f"A x B = {multiplicacao}")
    print()
    print("A multiplicaçaõ dos dois valores será representada pela letra C")
