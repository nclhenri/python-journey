"""
Refatorar: editar seu código.
"""
def soma(x , y, z = None):
    if z is not None:
        print(f"{x=} {y=} {z=}", x + y + z)
    else:
        print(f"{x=} {y=}", x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200, 0) # Se eu enviar um valor para z, 0 será assumido
# Se eu não enviar nenhum argumento, nesse cenário, None será assumido