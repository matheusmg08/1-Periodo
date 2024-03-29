#Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a. m.
print ('=' *50)
valor_depositado = float(input('Qual o valor que foi depositado?R$ '))
rendimento = valor_depositado + (valor_depositado * 0.007)
print(f'O seu novo valor considerando a taxa de juros de 0,70% ao mês é de R${rendimento:.2f}' )


