"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(nome, saudacao):
    def saudar():
        return f"{nome}, {saudacao}!"
    return saudar

saudacao1 = criar_saudacao("Nicolas", "Bom dia")
print(saudacao1())