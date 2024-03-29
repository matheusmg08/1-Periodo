"""
Faça um algoritmo que receba “N” números e mostre positivo, negativo ou zero para cada número
"""
n = int(input("Informe quantos números você desja verificar: "))
for i in range(n):
    numero = int(input("Informe um número: "))

    if numero > 0:
        print('Este número é positivo')
    elif numero < 0:
        print('Este número é negativo')
    else:
        print('O número é zero')