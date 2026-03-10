condicao = True
print("Caso queira sair, basta digitar 'sair'")
while condicao:
    nome = input("Qual é o seu nome:")
    if nome == "sair":
        break
    print(f"Seu nome é: {nome}")
print("Obrigado e até mais!")