produtos = [
    {"nome": "p1", "preco": 20,},
    {"nome": "p2", "preco": 10,},
    {"nome": "p3", "preco": 30,},
]

# nome_produto_lista = [nome_produto["nome"] for nome_produto in produtos] Código para pegar o produto pelo nome
# print(*nome_produto_lista, sep="\n")

nome_produto_lista = [{"nome": produto["nome"], "preco": produto["preco"]} for produto in produtos]
print(*nome_produto_lista)