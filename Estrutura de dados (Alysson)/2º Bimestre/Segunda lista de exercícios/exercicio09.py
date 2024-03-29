"""
Uma concessionária de veículos está vendendo os seus veículos com desconto. Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente de vários carros. O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%. O sistema deverá perguntar se deseja continuar calculando desconto até que a resposta seja: “(N) Não”. Informar total de carros com ano até 2000 e total geral.
"""
print("=" *70)
geral = 0
carros2000 = 0
resposta = input("Deseja calcular o desconto? (S) para sim ou (N) para não: ")

while resposta == "S":
    ano = int(input("Informe o ano do veículo: "))
    valor = float(input("Informe o valor do veículo: R$"))
    if ano <= 2000:
        desconto = valor * (0.12)
        final = valor - desconto
        print(f'Valor do desconto é: R$ {desconto:.2f}')
        print(f'Valor a ser pago é: R$ {final:.2f} ')
        carros2000 +=1
    else:
        desconto = valor *(0.07)
        final = valor - desconto
        print(f'Valor do desconto é: R$ {desconto:.2f}')
        print(f'Valor a ser pago é: R$ {final:.2f}')
        geral += 1  

    geral = carros2000 + geral
    print(f'Total de carros com ano até 2.000:{carros2000}')
    print(f'Total geral de carros: {geral}')


    resposta = input("Deseja continuar calculando o desconto? (S) para sim ou (N) para não: ")






