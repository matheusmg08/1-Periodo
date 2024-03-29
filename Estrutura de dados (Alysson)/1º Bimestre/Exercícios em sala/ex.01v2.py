#entrada de dados
print('-' *50)
altura = float(input('Digite sua altura em metros : '))
genero = input('Digite o genero (f) ou (m): ')
 #procesamento
peso_m = 72.7 * altura -58
peso_f = 62.1 * altura -44.7
#saida de dados
if genero == 'm' :
    print (f'Peso ideal de (m) , {peso_m:.1f} kg ')
else:
    print(f'Peso ideal (f) de {peso_f:.2f} kg ')

