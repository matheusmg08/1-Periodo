#A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra
print ('=' *50)
fatia_queijo = 2
fatia_presunto = 1
rodela_hamburguer = 1
quantidade_sanduiche = int(input('Quantos sanduíches serão feitos? '))
quantidade_queijo = quantidade_sanduiche * 50 * 2
quantidade_presunto = fatia_presunto * 50
quantidade_hamburguer = rodela_hamburguer * 100
queijo_kilo = quantidade_queijo / 1000
presunto_kilo = quantidade_presunto / 1000
hamburguer_kilo = quantidade_hamburguer / 1000
print (f'A quantidade de queijo utilizado será de {queijo_kilo} kg , de presunto será de {presunto_kilo} kg e de hambúrguer será de {hamburguer_kilo} kg.')


