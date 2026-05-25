# Exemplo de uso dos sets
letra_misteriosa = set()

while True:
    letra = input("Digite a letra: ")

    letra_misteriosa.add(letra)

    if "l" in letra_misteriosa:
        print("Você acertou!")
        break

    print(letra_misteriosa)

print("Saiu do laço")
