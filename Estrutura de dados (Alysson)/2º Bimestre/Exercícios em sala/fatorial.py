"""
Fatorial de um número , ex: definidio que 0!=1
definido que 1!= 1*0! = 1*1 = 1
exemplos:
2! = 2*1! = 2*1 = 2
3! = 3*2! = 3*2*1 = 6
4! = 4*3*2*1 = 24
5! = 5*4*3*2*1 = 120
"""
msg = 'Calcula Fatorial do número'
print("-"*len(msg))
print(msg)
numero = int(input('Informe o número: '))
fatorial = 1
contador = 1

while contador <= numero:
    fatorial = fatorial * contador
    contador += 1
print(f'O fatorial do número {numero} é {fatorial}')
print("-"*len(msg))

