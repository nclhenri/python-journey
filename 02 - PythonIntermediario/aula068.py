"""
Escopo global: É o escopo onde todo o código pode atingir
Escopo local: É o escopo onde apenas nomes do mesmo local 
podem ser alcançados
"""

x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
        x = 11
        y = 2
        print(x, y)

    outra_funcao()  

    print(x)

# print(x) Aqui irá dar um erro, a variavel x só existe dentro da função

escopo () # Preciso chamar a funçao para executá-la