#Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).
print('=' *50)
nome = input('Informe o nome do aluno: ')
primeira_nota = float(input('Informe a nota da primeira prova do semestre: '))
segunda_nota = float(input('Informe a nota da segunda prova do semestre: '))
terceira_nota = float(input('Informe a nota da terceira prova do semestre: '))
media = (primeira_nota + segunda_nota + terceira_nota) /3
print(f'O seu nome é {nome} , e sua média foi de {media} pontos !')


