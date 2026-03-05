"""
String são navegáveis por índices (iteráveis)
"""

nome = "Nicolas"
print(nome[2])
print(nome[-3])
print("c" in nome)
print("y" in nome)

print("c" not in nome)
print("y" not in nome)

nome1 = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}!")
else:
    print(f"{encontrar} NÃO está em {nome}!")