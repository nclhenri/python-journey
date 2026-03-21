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
primeiro_digito = 0 if resto > 9 else resto


print(f"O primeiro dígito do CPF é: {primeiro_digito}")

# --------------- Segundo Dígito --------------

cpf_10 = cpf_9 + str(primeiro_digito)

soma = 0
multiplicacao = 11
soma_resultado = 0

for numero in cpf_10:
    resultado = multiplicacao * int(numero)
    soma_resultado += resultado
    soma += int(numero)
    multiplicacao -= 1

multiplicar_resultado = soma_resultado * 10
resto = multiplicar_resultado % 11
segundo_digito = 0 if resto > 9 else resto

print(f"O Segundo dígito do CPF é: {segundo_digito}")