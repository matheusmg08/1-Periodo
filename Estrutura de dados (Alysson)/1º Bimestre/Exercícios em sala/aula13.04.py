"""
Identificar se o número é par :
"""
print('=' *100)
numero = int(input('Digite o valor: '))
resto = numero%2
if resto == 0:
    print(f'{numero} é um número par ')
print('Fim da execução')

print('=' *100)
# Testando condição , if , else
print('=' *100)
numero = int(input('Digite o valor: '))
resto = numero%2
if resto == 0:
    print(f'{numero} é um número par ')
else:
    print(f'{numero} é um número ímpar')    

# Programa para somar ou multiplicar dois números
opcao = input('S para somar ou M para multipicar: ')
numero1 = float(input('Primeiro número: '))
numero2 = float(input('Segundo número: '))
if opcao == 'S':
    resultado = numero1+numero2
    print(f'O resultado da soma é: {resultado}')
else:
    resultado = numero1*numero2
    print(f'O resultado da multiplicação é {resultado:.0f}')
print('=' *100)
    

        







