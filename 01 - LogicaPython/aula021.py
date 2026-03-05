entrada = input("[E]ntrar [S]air: ")
senha = input("Senha: ")

senha_permitida = "123456"

if entrada == "E" and senha == senha_permitida:
    print("Entrou")
else:
    print("Sair")

# Em and, todas as condições precisam ser verdadeiras para que execute o bloco de código
