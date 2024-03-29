"""
Codifique um algoritmo que exiba um histograma da variação da temperatura durante a semana. Por exemplo, se as temperaturas forem: 19, 21, 25, 22, 20, 17 e 15ºC, de domingo a sábado, respectivamente, o algoritmo deverá exibir:
D: *************
S: *************
T: ***************
Q: *************
Q: **********
S:********
S: **********
Suponha que as temperaturas sejam todas positivas e que nenhuma seja maior que 80ºC.
"""
domingo = int(input('Me informe a temperatura de domingo: '))
while domingo <= 0 or domingo > 80:
    domingo = int(input('Temperatura inválida, digite uma temperatura positiva até 80ºC: '))
segunda = int(input('Me informe a temperatura de segunda: '))
while segunda <= 0 or segunda > 80:
    segunda = int(input('Temperatura inválida, digite uma temperatura positiva até 80ºC: '))
terca = int(input('Me informe a temperatura de terça: '))
while terca <= 0 or terca > 80:
    terca = int(input('Temperatura inválida, digite uma temperatura positiva até 80ºC: '))
quarta = int(input('Me informe a temperatura de quarta: '))
while quarta <= 0 or quarta > 80:
    quarta = int(input('Temperatura inválida, digite uma temperatura positiva até 80ºC: '))
quinta = int(input('Me informe a temperatura de quinta: '))
while quinta <= 0 or quinta > 80:
    quinta = int(input('Temperatura inválida, digite uma temperatura positiva até 80ºC: '))
sexta = int(input('Me informe a temperatura de sexta: '))
while sexta <= 0 or sexta > 80:
    sexta = int(input('Temperatura inválida, digite uma temperatura positiva até 80ºC: '))
sabado = int(input('Me informe a temperatura de sábado: '))
while sabado <= 0 or sabado > 80:
    sabado = int(input('Temperatura inválida, digite uma temperatura positiva até 80ºC: '))

print ('Histrograma de temperatura semanal: ')
print (f'D: {"*" * domingo}')
print (f'S: {"*" * segunda}')
print (f'T: {"*" * terca}')
print (f'Q: {"*" * quarta}')
print (f'Q: {"*" * quinta}')
print (f'S: {"*" * sexta}')
print (f'S: {"*" * sabado}')








