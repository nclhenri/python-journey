"""
split - divide uma string
join - une uma string
"""

frase = "Olá, bom dia! Que dia lindo."
lista_palavras = frase.split(",") # O caracter colocado no parâmetro, NÃO será incluído
print(lista_palavras)

frases_unidas = "-".join(frase)
print(frases_unidas)