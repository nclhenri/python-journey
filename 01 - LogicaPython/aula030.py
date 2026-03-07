velocidade = 61
local_carro = 98

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print("Você ultrapassou o limite de velocidade!")

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and (velocidade > RADAR_1):
    print("Você passou acima do limite permitido e foi MULTADO!!")