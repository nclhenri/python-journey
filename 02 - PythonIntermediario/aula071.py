"""
args - Argumentos não nomeados
*args (empacotamento e desempacotamento)
"""

x, y, *resto = 1, 2, 3, 4 # O * em resto, indica que essa variável irá guardar o restante dos argumentos
print(x, y, resto)

def soma(*args): # Isso aqui EMPACOTA
    total = 0

    for numero in args:
        total += numero

    return total

soma1_2_3 = soma(1, 2, 3)
print(soma1_2_3)

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(*numeros) # Isso aqui '*' DESEMPACOTA 
# print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9)) ISSO DARÁ ERRO
print(sum(numeros)) # Isso dará CERTO