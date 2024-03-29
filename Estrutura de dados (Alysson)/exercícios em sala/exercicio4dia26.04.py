"""
Faça um programa que leia uum número inteiro entre 0 e 9999 e escreva seu valor por extenso
"""
valor = int(input('Digite um valor inteiro entre 0 e 9999: '))
if valor >= 0 and valor <= 9999:
    milhar = valor // 1000
    resto = valor % 1000
    centena = resto // 100
    resto = resto % 100
    dezena = resto // 10
    unidade = resto%10
    if milhar == 9:
        print('Nove mil', end=' ')
    elif milhar == 8:
        print('Oito mil', end=' ')
    elif milhar == 7:
        print('Sete mil', end=' ')
    elif milhar == 6:   
        print('Seis mil', end=' ')
    elif milhar == 5:
        print('Cinco mil', end=' ')   
    elif milhar == 4:
        print('Quatro mil', end=' ')
    elif milhar == 3:
        print('Três mil', end=' ')
    elif milhar == 2:
        print('Dois mil', end=' ')
    elif milhar == 1:
        print('Um mil', end=' ') 
    if milhar % 1000 != 1:
        print(',', end=' ')       

    if centena == 9:
        print('Novecentos', end=' ')
    elif centena == 8:
        print('Oitocentos', end=' ')
    elif centena == 7:
        print('Setecentos', end=' ')
    elif centena == 6:
        print('Seiscentos', end=' ')
    elif centena == 5:
        print('Quinhentos', end=' ')
    elif centena == 4:
        print('Quatrocentos', end=' ')
    elif centena == 3:
        print('Trezentos', end=' ')
    elif centena == 2:
        print('Duzentos', end=' ')
    elif centena == 1:
        print('Cem', end=' ')
    if centena % 100 !=1:
        print('e', end=' ')    

    if dezena == 9:
        print('Noventa', end=' ')
    elif dezena == 8:
        print('Oitenta', end=' ')
    elif dezena == 7:
        print('Setenta', end=' ')
    elif dezena == 6:
        print('Sessenta', end=' ')
    elif dezena == 5:
        print('Cinquenta', end=' ')
    elif dezena == 4:
        print('Quarenta', end=' ')
    elif dezena == 3:
        print('Trinta', end=' ')
    elif dezena == 2:
        print('Vinte', end=' ')
    elif dezena == 1:
        print('Dez', end=' ')
    if dezena != 1:
        print('e', end=' ')


    if unidade == 9:
        print('Nove', end=' ')
    elif unidade == 8:
        print('Oito', end=' ')
    elif unidade == 7:
        print('Sete', end=' ')
    elif unidade == 6:
        print('Seis', end=' ')
    elif unidade == 5:
        print('Cinco', end=' ')
    elif unidade == 4:
        print('Quatro', end=' ')
    elif unidade == 3:
        print('Três', end=' ')
    elif unidade == 2:
        print('Dois', end=' ')
    elif unidade == 1:
        print('Um' ,end=' ')   
                                                                                               

else:
    print('Você digitou um valor fora do intervalo! ')