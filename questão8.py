import os 


os.system("cls||clear")

print("""
        COR     |  PREÇO
        VERDE   | R$10,00
        AZUL    | R$20,00
        AMARELO | R$30,00
        VERMELHO| R$40,00


      """)
cor = str(input("Por favor diga qual a cor do CD que vc deseja:  ")).lower()


match cor:
    case "verde":
        valor = 10
    case "azul":
        valor = 20
    case "amarelo":
        valor = 30
    case "vermelho":
        valor = 40
    case _:
        print("Cor não encontrada")

print(f"A cor foi {cor} então o valor será: {valor}")
