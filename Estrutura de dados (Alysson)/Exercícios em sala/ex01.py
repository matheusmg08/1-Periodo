prova1 = ('Digite a nota da prova 1: ' (i)))
prova2 = int(input('Digite a nota da prova 2: '))
trabalho = int(input('Digite a nota do trabalho: '))
participacao = int(input('Digite a nota da participação: '))
provas = 3*prova1+3*prova2
media = (provas +3* trabalho + participacao) /10
print ('Sua média foi : {} ' .format(media))

