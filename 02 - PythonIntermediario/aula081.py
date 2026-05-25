"""
Operadores úteis (pt2):
União | - Unir sets
Intersecção & - Itens presentes em ambos os sets
Diferença - - Itens presentes apenas no set da esquerda
Diferença simétrica ^ - Itens que não estão em ambos
"""

s1 = {1, 2, 3}
s2 = {2, 3, 4}
# s3 = s1 | s2 # União (Retornar a união dos sets)
s3 = s1 & s2 # Intersecção (Retornará itens iguais de ambos os sets)
# s3 = s2 - s1   # Diferença (Retornará apenas o que tiver de EXCLUSIVO no set da esquerda da equação)
# s3 = s1 ^ s2 # Diferença simétrica (Retornará o que tiver de EXCLUSIVO em ambos os lados da equação)

print(s1)
print(s2)
print(s3)