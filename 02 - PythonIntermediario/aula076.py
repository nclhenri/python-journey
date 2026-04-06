pessoa = {
    "Nome:": "Nicolas Henrique",
    "Idade:": 22,
    "Apelidos:":[
        {"Jogos:": "Niquinha"},
        {"Trabalho:": "Nic"}
    ]
}

jogos = {}

jogos["nome"] = "Ride 4"
jogos["nome"] = "Left4Dead2"
# del jogos["nome"] Apagar

"""
Condição para saber se um dict existe:
if jogos.get("nome", "Não existe"):
    print("Existe!")
else:
    print(jogos["nome"])

.get - ele tenta OBTER o valor, se não tiver, retorna o valor da condição
"""

print(jogos) # {'nome': 'Left4Dead2'}
print(jogos["nome"]) # Left4Dead2

print(pessoa["Nome:"])
print(pessoa["Apelidos:"])

for chave in pessoa:
    print(chave)

for chave in pessoa:
    print(chave, pessoa[chave])