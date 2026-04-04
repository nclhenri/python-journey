"""
High Order Functions
Funções de Primeira Classe
"""

def saudacao(nome ,msg):
    return f"{nome}, a mensagem é: {msg}"

def funcao_nova(funcao_que_queremos, *args):
    return funcao_que_queremos(*args)



print(
    funcao_nova(saudacao, "Nicolas", "Olhe para trás.")
)