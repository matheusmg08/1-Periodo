"""
Programa que imprime a soma de todos os números pares entre dois números quaisquer , incluindo-os
"""

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
iterador = min(valor1,valor2)

soma = 0
while iterador <= max(valor1,valor2):
    if iterador % 2 == 0:
        soma = soma + iterador
    iterador = iterador + 1

print(f'A soma dos números pares entre {valor1} e {valor2} é {soma} !')