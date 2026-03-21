salas = [
    ["Nicolas", "Henrique"], # Indice 0
    ["Silva"], # Indice 1
    ["Brito", "Jordan", "Cage", (0, 1, 2, 3 ,4)] # Indice 2
]

print(salas[2][3][3])

for sala in salas:
    for aluno in sala:
        print(aluno)