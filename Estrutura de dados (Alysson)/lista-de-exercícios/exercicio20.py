#Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. Faça um programa para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais. Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. Não havendo moeda de um tipo, a quantidade respectiva é zero.
print ('=' *50)
um_centavo = int(input('Quantas moedas de 1 centavo tem no cofrinho? '))
cinco_centavos = int(input('Quantas moedas de 5 centavos tem no cofrinho? '))
dez_centavos = int(input('Quantas moedas de 10 centavos tem no cofrinho? '))
vinte_e_cinco_centavos = int(input('Quantas modedas de 25 centavos tem no cofrinho? '))
cinquenta_centavos = int(input('Quantas moedas de cinquenta cetavos tem no cofinho? '))
um_real = int(input('Quantas moedas de 1 real tem no cofrinho? '))
valor_total = (um_centavo * 0.01) + (cinco_centavos * 0.05) + (dez_centavos * 0.10) + (vinte_e_cinco_centavos * 0.25) + (cinquenta_centavos * 0.5) + (um_real * 1)
print(f'O valor economizado foi de R${valor_total:.2f} ')





