"""
Iterando strings com while
"""

nome = "Nicolas Henrique"
tamanho_nome = len(nome)

print(nome)
print(tamanho_nome)

contador = 0
novo_nome = ""
while contador < tamanho_nome:
    letra = nome[contador]
    novo_nome += letra
    contador += 1
print(novo_nome)