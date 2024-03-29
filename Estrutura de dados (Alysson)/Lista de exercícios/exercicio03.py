# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.
print('=' *50)
custo_fabrica=float(input('Informe o valor do custo de fábrica do carro: '))
distribuidor = custo_fabrica*(28/100)
imposto = custo_fabrica*(45/100)
custo_consumidor = custo_fabrica + distribuidor + imposto
print(f'O custo de fábrica do carro é R${custo_fabrica} e o custo ao consumidor é R${custo_consumidor:.2f}. ')



