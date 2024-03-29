"""
DESAFIO!!!
Como fazer para contar a quantidade de números pares entre dois números quaisquer ?

"""

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
par = 0

if num_2 < num_1 :
    primeiro = num_2
    segundo = num_1
else:
    primeiro = num_1
    segundo = num_2

while primeiro <= segundo:
    if primeiro %2 == 0:
        par +=1
    primeiro +=1
    
print(f'Existem {par} números pares ! ')            

