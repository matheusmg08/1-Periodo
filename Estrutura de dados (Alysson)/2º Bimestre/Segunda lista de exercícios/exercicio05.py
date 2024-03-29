"""
Faça um programa que calcule e mostre a média aritmética de N notas. N equivale ao total de avaliações.
"""
nota = int(input('Digite a nota que será calculado a média: '))
soma = 0
for i in range (nota):
    notas = int(input(f'Digite a nota da avaliação {i}: '))
    soma += notas
media = soma / nota
print(f'A média das notas é {media}')
