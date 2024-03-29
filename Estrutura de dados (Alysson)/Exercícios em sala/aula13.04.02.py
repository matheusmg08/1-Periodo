# Programa para somar ou multiplicar dois números
opcao = input('S para somar ou M para multipicar: ')
numero1 = float(input('Primeiro número: '))
numero2 = float(input('Segundo número: '))
if opcao == 'S':
    resultado = numero1+numero2
    print(f'O resultado da soma é: {resultado}')
elif opcao  == 'M':
    resultado = numero1*numero2
    print(f'O resultado da multiplicação é {resultado:.0f}')
else:
    print('Opção inválida')    
print('=' *100)
