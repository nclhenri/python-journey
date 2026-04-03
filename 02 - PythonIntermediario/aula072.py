"""
Exercícios com funções

1. Crie uma função que multiplica todos os argumentos não nomeados recebidos.
2. Retorne o total para uma variável e mostre o valor da variável.
3. Crie uma função que fala se o número é par ou ímpar.
4. Retorne se o número é par ou ímpar.
"""

def multiplicacao(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

numeros = 2, 2, 2, 2, 2

print(multiplicacao(*numeros))

def par_ou_impar(*args):
    resultado = []
    for numero in args:
        if numero % 2 == 0:
            resultado.append(f"{numero} é PAR!")
        else:
            resultado.append(f"{numero} é ÍMPAR!")
    return resultado

valores = 1, 2, 3

for item in par_ou_impar(*valores):
    print(item)