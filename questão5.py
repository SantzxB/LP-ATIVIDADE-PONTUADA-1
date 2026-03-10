import os 


os.system("cls||clear")

nA = int(input("Digite um valor:   "))
nB = int(input("Digite outro Valor:   "))
caracter =str (input("Digite a operação desejada:  "))

match caracter:
    case "+":
        print(nA+ nB)
    case "-":
        print(nA - nB)
    case "*":
        print(nA *nB)
    case "/":
        print(nA / nB)
    case _:
        print("operação inválida.")
