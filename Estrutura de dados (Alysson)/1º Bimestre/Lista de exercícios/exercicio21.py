#Uma loja de roupas está fazendo uma liquidação e está oferecendo um desconto de 30% em todas as peças. Faça um programa em que o vendedor informe o valor da roupa e o programa retorna quanto ela custará durante a liquidação?
print ('=' *50)
valor_roupa = float(input('Qual o valor da roupa? '))
total = valor_roupa - (valor_roupa * 0.30)
print (f'O preço da roupa com o desconto será de R${total:.2f}.')

