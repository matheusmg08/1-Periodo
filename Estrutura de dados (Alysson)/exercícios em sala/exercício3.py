# Entrada de dados
print ("-")
import math
lat1 = float(input('Latitude do ponto 1:  '))
long1 = float(input('Longitude do ponto 1: '))
print ("-")
lat2 = float(input('Latitude do ponto 2: '))
long2 = float(input('Longitude do ponto 2: '))
# Processamento
# Sqrt - square root > sigifica raiz quadrada
distancia = math.sqrt((lat1 - lat2)**2 + (long1 - long2)**2)
# Saída de dados
print (f'A distância entre o ponto 1 ({lat1} , {long1}) e o ponto 2 ({lat2} , {long2}) é {distancia}')








