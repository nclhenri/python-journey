numero = input("Digite um número para dobrar:")

try:
    int_numero = int(numero)
    print(f"O dobro de {numero} é: {int_numero * 2}")
except:
    print("Você não digitou um número!")