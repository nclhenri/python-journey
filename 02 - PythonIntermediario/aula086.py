# Empacotamento e desempacotamento

# Primeiro criamos duas dict

pessoa = {
	"nome": "Nicolas",
	"sobrenome": "Henrique"
}

info = {
	"idade": 22,
	"altura": 1.8
}

# Agora criaremos uma dict que una as duas

dados_completos = {**pessoa, **info}

print(dados_completos)

#------------------------------------------

def mostro_argumentos_nomeados(**kwargs):
    print(kwargs)

mostro_argumentos_nomeados(nomes="Nicolas", idades = 22)