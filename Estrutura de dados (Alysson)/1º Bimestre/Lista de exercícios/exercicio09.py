#Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.
print('=' *50)
litro = float(input('Me informe o preço do litro da gasolina onde vai abastecer:R$ '))
pagamento = float(input('Me informe quantos reais você vai colocar de gasolina:R$ '))
quantidade = pagamento / litro
print(f'Colocando R${pagamento} de gasolina, e pagando R${litro} no litro , você vai conseguir colocar {quantidade} litros no tanque!')



