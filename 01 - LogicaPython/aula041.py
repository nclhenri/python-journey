nome = "Nicolas Henrique"
tamanho_nome = len(nome)

i = 0

while i < tamanho_nome:
    print(nome[i])

    break # Já pula para fora do while

    i += 1
else:
    print("O else foi executado")
print("Fora do While")