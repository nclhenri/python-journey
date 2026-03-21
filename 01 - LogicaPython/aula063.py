cpf = "634892321"

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
str_primeiro_digito = str(primeiro_digito)

# --------------- Segundo Dígito --------------

cpf_10 = cpf_tratado + str(primeiro_digito)

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
str_segundo_digito = str(segundo_digito)

print(f"Os dígitos para esse CPF são: {primeiro_digito ,segundo_digito}")