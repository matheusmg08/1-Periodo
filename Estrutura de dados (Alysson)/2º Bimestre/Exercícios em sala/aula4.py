"""
DESAFIO!!!
Como fazer para contar a quantidade de números pares entre dois números quaisquer ?

"""

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
contador = min(num_1,num_2)

par = 0
while contador <= max(num_1,num_2):
    if contador%2 == 0:
        par += 1
        print(f'{contador} par')
    else:
        print(f'{contador} impar')

    contador = contador + 1
print(f'Temos {par} numeros pares neste intervalo')
   