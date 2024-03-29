"""
Faça um algoritmo que receba a idade de 75 pessoas e mostre mensagem informando “maior de idade” e “menor de idade” para cada pessoa. Considere a idade a partir de 18 anos como maior de idade.
"""
print("=" *70)
for i in range (75):
    idade = int(input("Digite a idade: "))

    if idade >= 18:
        print('Maior de idade')
    else:
        print('Menor de idade')
