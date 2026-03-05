nome = input("Digite seu nome: ")
idade = input("Digite a sua idade: ")

indice_nome = len(nome)

if nome and idade:
    print("Seu nome é:", nome)
    print("Seu nome invertido é:", nome[::-1])

    if " " in nome:
        print("Seu nome contém espaços!")
    else:
        print("Seu nome não contém espaços!")

    print(f"Seu nome tem {len(nome)} letras")
    print("A primeira letra do seu nome:", nome[0])
    print("A última letra do seu nome:", nome[indice_nome-1])
else:
    print("Desculpe, você deixou campos vazios!!")