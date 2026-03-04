n1 = input("Digite o primeiro valor: ")
n2 = input("Digite o segundo valor: ")

int_n1 = int(n1)
int_n2 = int(n2)

if n1 > n2:
    print(f"O {n1=} é maior que o {n2=}!")
elif n2 > n1:
    print(f"O {n2=} é maior que o {n1=}!")
else:
    print("Os valores são iguais!")