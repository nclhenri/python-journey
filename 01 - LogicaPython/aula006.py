"""
Não posso escrever print('1' + 1)
No Python, não é permitido concatenar dados do tipo int com dados do tipo str.
Esse comando resultará em erro.
"""

print(1 + 1)
# Aqui soma normal, números inteiros tipados dinâmicamente.

print("a" + "b")
# Aqui ocorre a concatenação. Resultado da execução: ab

print(int("1"), type(int("1")))
# Aqui ocorreu a converão de tipo, o 1 que era str passou a ser um inteiro.

print(float('1') + 1)  
# Soma os valores convertendo '1' em float e adicionando 1

print(bool(''))
# Convertendo uma str vazia para bool. Resultado será False

print(bool(' '))
# Convertendo uma str com um espaço para bool. Resultado será True

print(str(11) + "b")
# Convertendo o 11 para str e concatenando com o valorb. Resultado 11b