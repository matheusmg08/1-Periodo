#Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em 15%. Após o aumento, desconte 8% de impostos. Imprima o salário inicial, o salário com o aumento e o salário final.
print ('=' *50)
salario_inicial = float(input('Qual seu salário? R$ '))
aumento = salario_inicial * 0.15
aumento_total = salario_inicial + aumento
salario_final = aumento_total * 0.08
salario_final2 = aumento_total - salario_final

print (f'Seu salário inicial era de R${salario_inicial:.2f} , com o aumento subiu para R${aumento_total:.2f} e com o desconto de 8% , o salário final será de R${salario_final2:.2f} ')