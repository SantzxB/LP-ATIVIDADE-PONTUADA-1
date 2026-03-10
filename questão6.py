import os 


os.system("cls||clear")

nota1 = int(input("Coloque sua primeira nota:  "))
nota2 = int(input("Coloque sua segunda nota:  "))


media = (nota1 + nota2) / 2

if media >= 6:
    print(f"Sua Média é : {media}")
    print("Parabéns!")
elif media == 4:
    print(f"Sua Média é : {media}")
    print("Infelizmente você está em recuperaçaõ.")
else:
    print(f"Sua Média é : {media}")
    print("VOCÊ ESTÁ REPROVADO.")
