#Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
print('=' *50)
preco_custo = float(input('Qual o valor do preço de custo desse produto? '))
porcentagem_usuario = float(input('Qual a porcentagem que você deseja acrescentar no produto? '))
acrescimo = preco_custo * (porcentagem_usuario/100)
valor_venda = preco_custo + acrescimo
print(f'O valor de venda será de R${valor_venda:.2f} ')

