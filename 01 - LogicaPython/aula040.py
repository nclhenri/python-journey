# Calculadora com while

print("Para cancelar a operação digite: 0")
n1 = input("Digite o primeiro número:")
n2 = input("Digite o segundo número:")

try:
    int_n1 = int(n1)
    int_n2 = int(n2)
    while (int_n1 != 0) and (int_n2 != 0):
        opcao_escolhida = input("Escolha o símbolo da operação: + - * /:")

        operadores_permitidos = "+-/*"

        if operadores_permitidos not in opcao_escolhida:
            print("Você digitou um operador inválido!")

        if opcao_escolhida == "+":
            resultado = int_n1 + int_n2
            print(f"A soma entre {int_n1} e {int_n2} é: {resultado}")
        elif opcao_escolhida == "-":
            resultado = int_n1 - int_n2
            print(f"A subtração entre {int_n1} e {int_n2} é: {resultado}")
        elif opcao_escolhida == "*":
            resultado = int_n1 * int_n2
            print(f"A multiplicação entre {int_n1} e {int_n2} é: {resultado}")
        elif opcao_escolhida == "/":
            resultado = int_n1 / int_n2
            print(f"A divisão entre {int_n1} e {int_n2} é: {resultado}")
        n1 = int(input("Digite o primeiro número:"))
        n2 = int(input("Digite o segundo número:"))
except:
    print("Você digitou algum valor inválido!")
print("Obrigado e até logo!")

