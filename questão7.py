import os 

os.system("cls||clear")


print("""
          VOCÊ ESTÁ ADQUIRINDO NOSSO PRODUTO
     
     
         Gostaria de adquirir quantas unidades?
      """)
quantidade = int(input(""))

preco_UN = 209.00
total = quantidade * preco_UN

if quantidade <= 5:
    valor = total - 2
elif quantidade > 5 and quantidade <= 10:
    valor = total - 3
else:
    valor = total - 5

print()
print(f"Valor total: {total}")
print()
print("Foi aplicado desconto")
print(f"Valor com desconto: {valor}")
