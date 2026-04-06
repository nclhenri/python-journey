"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario com outro
"""

pessoa = {
    "Nome:": "Nicolas Henrique",
    "Idade:": 22
}

print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))
print(pessoa.setdefault("Sobrenome:", "Não existe um sobrenome"))
print(pessoa.get("Nome:", "Não existe um nome"))
# nome = pessoa.pop("Nome:") Ele pega o valor para si e exclui o valor no dicionario
# ultima_chave = pessoa.popitem() Ele pega o valor para si e exclui o ULTIMO valor no dicionario
pessoa.update({
    "Nome:": "Nicolas Novo"
})
print(pessoa)

"""
Shallow Copy
"""

import copy
d1 = {
    "c1": 1,
    "c2": 2,
    "l1": [0, 1, 2]
}

# d2 = copy.deepcopy(d1) Serve para fazer uma cópia profunda.
# Importante lembrar do import la em cima para usar o método

d2 = d1.copy() # Se eu tivesse uma lista dentro de d1 ele não IRÁ COPIAR, vai apenas linkar uma com a outra
# Se uma lista for mudada para um, o mesmo servirá para outro
d2["c1"] = 1000
d2['l1'][0] = 9999

print(d1)
print(d2)