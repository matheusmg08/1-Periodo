#A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.
print('=' *50)
valor_compra = float(input('Me informe qual o valor da sua compra:R$ '))
prestacoes = valor_compra / 5
print(f'Com a sua compra no valor de R${valor_compra:.2f} , as prestações vão ficar 5x de R${prestacoes:.2f}')

