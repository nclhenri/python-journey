frase = "Nicolas Henrique da Silva Brito"

indice = 0
quantidade_apareceu = 0
letra_apareceu = " "

while indice < len(frase):
    letra_atual = frase[indice]

    if letra_atual == " ":
        indice += 1
        continue

    quantidade_atual = frase.count(letra_atual)

    if quantidade_apareceu <= quantidade_atual:
        quantidade_apareceu = quantidade_atual
        letra_apareceu = letra_atual
    indice += 1

print(f"A letra que mais apareceu foi {letra_apareceu.upper()} com a quantidade de {quantidade_apareceu} vezes.")