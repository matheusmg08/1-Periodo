#Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto .
print('='*50)
distancia=float(input('Informe a distância total percorrida em km: '))
combustivel=float(input('Informe o total de combustível gasto em litros: '))
consumo = distancia/combustivel
print(f'O consumo médio do automóvel foi de {consumo:.2f} km/l. ')

