#Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina informe quanto será o valor arrecadado.
print ('=' *50)
camisetas_pequenas = int(input('Qual a quantidade de camisetas pequenas vendidas? '))
camisetas_medias = int(input('Qual a quantidade de camisetas médias vendidas? '))
camisetas_grandes = int(input('Qual a quantidade de camisetas grandes vendidas? '))
pequenas_vendidas = camisetas_pequenas * 10
medias_vendidas = camisetas_medias * 12
grandes_vendidas = camisetas_grandes * 15
total = pequenas_vendidas + medias_vendidas + grandes_vendidas
print (f'O total de arrecadação foi de R${total:.2f} ') 

