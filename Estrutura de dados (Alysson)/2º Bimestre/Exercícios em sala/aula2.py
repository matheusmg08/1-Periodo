"""
Programa que imprime a quantidade de números pares de 100 até 200, incluindo-os
"""
contador = 100
par = 0
while contador <=200:
    if contador % 2 == 0:
        par +=1
    contador +=1

print (f'Existem {par} números pares entre 100 e 200 ! ')    

print('=' *165)

contador = 100
par = 0
while contador <= 200:
    # é par quando o resta da divisão por 2 é 0
    if contador % 2 == 0:
        par += 1
    contador = contador + 1

print (f'Existem {par} números pares ! ')    

        



