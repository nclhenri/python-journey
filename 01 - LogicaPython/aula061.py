"""
Anotações:
1. Tratar o CPF informado (Tira pontos e traço)
2. Selecionar o primeiros 9 digitos do cpf
3. Somá-los
4. Multiplicar cada dígito por 10-1 cada volta
5. Somar cada resultado da multiplicação
6. Multiplicar essa soma por 10
7. Obter o resto da divisão da conta anterior por 11
8. Se o resultado anterior for maior que 9, retornar 0, se não, retorna o resto
"""

cpf = "746.824.890-70"

cpf_tratado = cpf.replace(".", "").replace("-", "")

cpf_9 = cpf_tratado[:9]

soma = 0
multiplicacao = 10
soma_resultado = 0

for numero in cpf_9:
    resultado = multiplicacao * int(numero)
    soma_resultado += resultado
    soma += int(numero)
    multiplicacao -= 1

multiplicar_resultado = soma_resultado * 10
resto = multiplicar_resultado % 11

print(f"A soma dos primeiros 9 digitos do CPF é: {soma}")
print(f"A soma das multiplicações: {soma_resultado}")
print(f"A multiplicação da soma: {multiplicar_resultado}")
print(f"O resto da divisao: {resto}")

print(f"O primeiro dígito do CPF é: {0 if resto > 9 else resto}")
