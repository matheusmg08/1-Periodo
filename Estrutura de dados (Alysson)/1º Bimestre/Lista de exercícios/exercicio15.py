#Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida ela possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa com 19 anos possui 6935 dias de vida; veja um exemplo de saída: Ex: Tibúrcio, você já viveu 6935 dias.
print ('=' *50)
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
anos_vividos = idade * 365
print(f'{nome} , você já viveu {anos_vividos} dias.')



