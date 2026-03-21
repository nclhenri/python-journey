lista = ["Nicolas", "Henrique", 1, 2, 3, "Jordan"]
tupla = "Gosto",  "Muito", "de", "estudar!"
a, b, *_, c, d = lista
print(a, c, d)
print(tupla)

print(*lista) # Cada item da lista vai ser exibido na mesma linha