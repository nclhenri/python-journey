"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.
"""

def duplicar(*args):
    resultados = []
    for numero in args:
        resultado = numero * 2
        print(f"O {numero} duplicado fica: {resultado}")
        resultados.append(resultado)
    return resultados

valores = 9, 4, 7
resultado = duplicar(*valores)
print(f"Resultados finais {resultado}")
print(" ")

def triplicar(*args):
    resultados = []
    for numero in args:
        resultado = numero * 3
        print(f"O {numero} triplicado fica: {resultado}")
        resultados.append(resultado)
    return resultados

valores = 9, 4, 7
resultado = triplicar(*valores)
print(f"Resultados finais {resultado}")
print(" ")

def quadruplicar(*args):
    resultados = []
    for numero in args:
        resultado = numero * 3
        print(f"O {numero} quadruplicado fica: {resultado}")
        resultados.append(resultado)
    return resultados

valores = 9, 4, 7
resultado = quadruplicar(*valores)
print(f"Resultados finais {resultado}")
print(" ")