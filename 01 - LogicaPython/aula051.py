nome1, nome2, nome3 = ["Nicolas", "Henrique", "Silva"]
# nome1, nome2 = ["Nicolas", "Henrique", "Silva"] Valores demais para poucas variaveis
# nome1, nome2, nome3, nome4 = ["Nicolas", "Henrique", "Silva"] Variaveis demais para poucos valores
nome1, *resto = ["Nicolas", "Henrique", "Silva"]
nome1, *_ = ["Nicolas", "Henrique", "Silva"] # _ = convenção usada por dev para resto
_,nome1, *_ = ["Nicolas", "Henrique", "Silva"] 
print(nome1)