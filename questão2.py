import os 

os.system("cls||clear")

sexo_F = str("feminino")
casada = str("casada")

nome = str(input("Digite seu nome:"))
sexo = str(input("Digite seu sexo:")).lower()
estado_civil = str(input("Digite seu estado civil:")).lower()

if sexo == sexo_F and estado_civil == casada:
    tempo_casada = int(input("Quanto anos casada?"))

print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estado_civil} ")

