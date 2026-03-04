nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
# Para fazer o input de inteiros, precisa-se fazer o casting primeiro
"""
Não é prudente fazer o casting da variável tudo na mesma linha. O certo é:
1. Pegar o valor do input como str.
n1 = input("Digite o primeiro número:")
2. Pós isso, fazer o casting a parte:
int_n1 = int(n1)
3. Feito isso, você vai tratar o que era str em int.
"""

soma = n1 + n2

print(f"O seu nome é {nome} e a sua idade é {idade}")
print(f"A soma dos números é {soma}")