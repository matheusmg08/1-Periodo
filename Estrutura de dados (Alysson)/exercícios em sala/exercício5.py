# Entrada de dados
print("----- DPM - Dispensador Preciso de Moedas -----")        
valor=int(input('Informe um valor em centavos: '))
print('------------------------')
moedas_1real = valor // 100
resto = valor % 100
moedas_50cents = resto // 50
resto = resto % 50
moedas_25cents = resto // 25
resto = resto % 25
moedas_10cents = resto // 10
resto = resto % 10
moedas_5cents = resto // 5
moedas_1cent = resto % 5
print(f'{moedas_1real} moedas de R$ 1,00')
print(f'{moedas_50cents} moedas de R$ 0,50')
print(f'{moedas_25cents} moedas de R$ 0,25')
print(f'{moedas_10cents} moedas de R$ 0,10')
print(f'{moedas_5cents} moedas de R$ 0,05')
print(f'{moedas_1cent} moedas de R$ 0 ,01')




