#Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados. Ex: Início A vale 3 e B vale 5 no final da execução A valerá 5 e B valerá 3.
print('=' *50)
a_inicio = int(input('Informe o valor de A: '))
b_inicio = int(input('Informe o valor de B: '))
a_final = b_inicio
b_final = a_inicio
print(f'No início , A valia {a_inicio} e B valia {b_inicio} , agora o valor de A é {a_final} e o valor de B é {b_final} .')

