
"""
lista = ["Nicolas", 22, 2.2, True] # Criar

print("Essa é a lista antes da alteração:")

print(lista)

print(lista) # Ler

lista[0] = "Henrique" # Alterar

del lista[0] # Apagar 

lista.append(20) # Adiciona o valor ao final da lista (último índice)

lista.pop() # Remove o último item da lista ou uma valor especifico no parametro

# del lista[-1] # Remove o último item da lista, independente da quantidade

# lista.clear() # Limpa a lista por completo

lista.insert(0, 5) # Inserir no indice 0 o valor 5

print("Essa é a lista depois da alteração:")

print(lista)
"""

"""
Assim que eu apagar o indice 0, o indice 1 assume o 0 de forma imediata
Ou seja: 
0          1   2
Henrique, 22, 2.2
Assim que o Henrique for apagado, o valor "22", assumirá o indice 0
"""

"""
lista_a = [1,2,3]

lista_b = [4,5,6]

lista_c = lista_a + lista_b # Concatena a lista

lista_a.extend(lista_b) # Estende a lista

print(lista_a)

print(lista_c)
"""

lista_a = ["Nicolas", "João"]
lista_b = lista_a.copy() # Copia a lista A para a lista B

lista_a[0] = "Henrique"
print(lista_a)
print(lista_b)