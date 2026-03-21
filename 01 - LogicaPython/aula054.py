print("Bem-Vindo a Lista de Compra!")
print("Para começar nos informe o que deseja fazer:")
print("i - para inserir")
print("a - para apagar")
print("l - para listar")
print("s - para sair")

entrada_usuario = input("")
itens = []

while entrada_usuario != "s":

    if entrada_usuario == "i":
        valor = input("Digite o nome do produto:")
        itens.append(valor)
    
    elif entrada_usuario == "l":
        if not itens:
            print("Não há nada para ser mostrado!")
        else:
            for indice, nome in enumerate(itens):
                print(indice, nome)
    
    elif entrada_usuario == "a":
        indice = input("Digite o valor do indice:")
        int_indice = int(indice)
        del itens [int_indice]
    
    
        
    print("i - para inserir")
    print("a - para apagar")
    print("l - para listar")
    print("s - para sair")
    entrada_usuario = input("")
print("Até logo!")