contador = 0

while contador < 10:
    contador += 1
    
    if contador == 3:
        continue #Esse comando faz com que o programa volte para o laço (para cima)
    
    print(contador)

    if contador == 4:
        break # Esse comando quebra o laço independente da condição ser verdadeira ou não
print("Saiu do laço")