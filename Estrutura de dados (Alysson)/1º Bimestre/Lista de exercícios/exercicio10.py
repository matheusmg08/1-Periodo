#Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês.
print('=' *50)
nome = input('Qual seu nome? ')
salario_fixo = float(input('Me informe seu salário fixo:R$ '))
vendas = float(input('Qual o valor em dinheiro , que você vendeu no mês?R$ '))
salario_final = salario_fixo + (vendas *0.15)
print(f'Seu nome é {nome} , seu salário fixo é R${salario_fixo} e o total do seu salário no final do mês será de R${salario_final} ')






