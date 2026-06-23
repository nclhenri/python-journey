numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Criação simples de uma lista

dobro = [n * 2 for n in numeros] # declara a expressão e para cada item da lista realizá-la

print(dobro) # mostrar o resultado

numeros_parte_dois = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

par = ["par" if n % 2 == 0 else "impar" for n in numeros_parte_dois] # par se a primeira
# parte da expressão for verdadeira, se não, mostrará ímpar para cada item
# na lista numeros_parte_dois

print(par) # mostra o resultado