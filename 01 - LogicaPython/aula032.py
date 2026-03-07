# Usuário digitar um número inteiro e informar se é par ou impar. Se nao for um numero, avise.
"""
n1 = input("Digite um número: ")
try:
    int_n1 = int(n1)
    
    if int_n1 % 2 == 0:
        print(f"O número: {int_n1} é PAR!")
    else:
        print(f"O número: {int_n1} é ÍMPAR!")

except:
    print("O valor digitado não é um número!")

"""

# Usuario digita a hora e da bom dia, boa tarde ou boa noite

"""
hora = input("Digite a hora: ")

try:
    int_hora = int(hora)

    if (int_hora >= 0) and (int_hora <= 11):
        print("Bom dia!")
    elif (int_hora >= 12) and (int_hora <= 18):
        print("Boa tarde!")
    else:
        print("Boa Noite!")
except:
    print("Você não digitou um valor válido!")
"""

# Nome curto, normal e grande

nome = input("Digite seu nome: ")
tamanho_nome = len(nome)

if (tamanho_nome <= 4):
    print("Seu nome é curto!")
elif(tamanho_nome >= 5) and (tamanho_nome <= 6):
    print("Seu nome tem tamanho normal!")
else:
    print("Seu nome é grande!")