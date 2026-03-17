tentativas = 0
palavra_secreta = "ola"
letra_acertada = ""
tentativa = input("Digite seu primeiro chute:")

while tentativa != palavra_secreta:
    if len(tentativa) > 1:
        print("Você digitou mais de uma letra")
        tentativas += 1
        tentativa = input("Tente outra vez!:")
        continue
    
    if tentativa in palavra_secreta:
        print(f"A letra '{tentativa}' contêm na frase.")
        letra_acertada += tentativa
    else:
        print(f"A letra '{tentativa}' NÃO contêm na frase.")

    palavra_formada = ""

    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print(f"Palavra formada: {palavra_formada}")
    tentativa = input("Tente outra vez!:")
    
    tentativas += 1

print(f"Você acertou!! A palavra correta era '{palavra_secreta}'")
print(f"Você precisou de {tentativas} tentativas!")
