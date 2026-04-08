"""
Métodos úteis
"""
s1 = set() # Se eu quiser criar um set vazio
s1.add("Nicolas") # Adicionar valor no set (Essa função aceita um valor por vez)
s1.add("Outro valor")
s1.update(("Olá, mundo!", 1)) # Para passar em ordem, precisa de um elemento iterável
# s1.clear() # Vai limpar o set
s1.discard("Olá, mundo!") # Passar o valor que você quer descartar
print(s1)