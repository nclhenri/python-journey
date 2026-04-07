perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

quantidade_acertos = 0

for pergunta in perguntas:
    print(pergunta["Pergunta"])
    print()

    opcoes = pergunta["Opções"]
    for i, opcao in enumerate(opcoes):
        print(f"{i}) {opcao}")
    print()

    escolha = input("Qual a sua escolha?: ")

    acertou = False
    quantidade_opcoes = len(opcoes)
    int_escolha = int(escolha)

    if escolha.isdigit():
        int_escolha = int(escolha)
        if (int_escolha >=0) and (int_escolha <= quantidade_opcoes):
            if opcoes[int_escolha] == pergunta["Resposta"]:
                acertou = True
    
    if acertou:
        quantidade_acertos += 1
        print("Você acertou! :D ")
    else:
        print("Você errou! :(")

print("Você acertou", quantidade_acertos, "de", len(perguntas))