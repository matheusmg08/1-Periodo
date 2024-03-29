#O restaurante a quilo Bem-Bão cobra R$19,00 por cada quilo de refeição. Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e escreva o valor a pagar. Assuma que a balança já desconte o peso do prato.
prato_cliente = float(input('Qual o peso em kg , do seu prato montado? '))
peso_prato = 1
peso_total = (prato_cliente * 19) - peso_prato * 19
print(f'O valor a pagar será de R${peso_total:.2f} , já descontando {peso_prato} kg do peso do prato vazio ')




