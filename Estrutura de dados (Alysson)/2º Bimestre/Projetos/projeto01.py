"""
Desenvolva um jogo da forca em python, no qual o programa escolhe aleatoriamente uma palavra secreta de um conjunto pré-definido. O jogador deve tentar advinhar a palavra digitando letras. Se a letra esrtiver na palavra secreta, ela deve ser revelada nas posições corretas. Caso contrário, o jogador perde uma vida. O jogo continua até que o jogador advinhe corretamente a palavra secreta ou perca todas as vidas. O número máximo de vidas deve ser definido pelo programador. O jogo deve exibir uma "representação" da forca conforme o jogador erra letras. Ao final do jogo, o programa deve informar se o jogador venceu ou perdeu, e perguntar se deseja jogar novamente.
"""
import os
import requests
import random

url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'

response = requests.get(url)
palavras = response.text.split('\n')
opcao = 'S'

while opcao == 'S':
    sorteada = random.choice(palavras).upper()
    print (sorteada)
    palavra = '*'*len(sorteada)
    tentativas = []
    vida = 10
    while vida > 0  and  palavra.count('*') != 0:
        os.system('cls')
        print (palavra)
        print (f'Vidas restantes: {vida}')
        print (f'Letras digitadas erradas:{tentativas}')
        letra = input('Digite uma letra: ').upper()
        while len(letra)>1:
            print('Formato inválido, tente novamente.')
            letra = input('Digite uma letra: ').upper()
        while letra in tentativas or letra in list(palavra):
            print (f'Letra {letra} já foi digitada, tente outra letra.')
            letra = input('Digite uma letra: ').upper()
        auxiliar = list(palavra)
        for x in range(len(sorteada)):
            if letra == sorteada[x]:
                auxiliar[x] = letra
                palavra = ''.join(auxiliar)
                print (palavra)
        if sorteada.count(letra) == 0:
            vida -= 1
            tentativas.append(letra)
            
    if vida == 0:
        os.system('cls')
        print(f'Que pena, você perdeu, a palavra era {sorteada}')
    else:
        os.system('cls')
        print (palavra)
        print('PARABÊNS você ganhou!!!')
    opcao = input('Deseja jogar novamente? "S" ou "N": ').upper()
    while opcao != 'S' and opcao != 'N':
        print('Opção inválida, tente novamente.')
        opcao = input('Deseja jogar novamente? "S" ou "N"').upper()
if opcao == 'N':
    print('Obrigado por ter utilizado nosso sistema!!!')