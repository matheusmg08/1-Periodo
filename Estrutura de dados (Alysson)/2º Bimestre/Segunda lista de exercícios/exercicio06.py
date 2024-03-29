"""
Escrever um algoritmo que lê o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula:
MA = (Nota1 + Nota2 * 2 + Nota3 * 3 + ME)/7
A atribuição de conceitos obedece a tabela abaixo:
Média de Aproveitamento | Conceito
MA >= 9,0               | A
7,5 <= MA < 9,0         | B
6,0 <= MA < 7,5         | C
4,0 <= MA < 6,0         | D
MA < 4,0                | E
O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a mensagem: APROVADO se o conceito for A, B ou C e REPROVADO se o conceito for D ou E. Pergunte se o usuário deseja digitar as notas de outro aluno S para sim e N para não
"""
opcao = "S"
while opcao == "S":

    numeroid = float(input('Informe seu número de identificação: '))
    nota1 = float(input('Informe a nota da primeira prova: '))
    nota2 = float(input('Informe a nota da segunda prova: '))
    nota3 = float(input('Informe a nota da terceira prova: '))
    me = float(input('Digite a média dos exercícios: '))
    mediaproveitamento = int(nota1 + (nota2 * 2) + (nota3 * 3) + me) /7
    conceito = ''
    if mediaproveitamento >= 9.0:
        conceito = "A"
    elif mediaproveitamento >= 7.5:
    
        conceito = "B"
    elif mediaproveitamento >= 6.0:
        conceito = "C"
    elif mediaproveitamento >= 4.0:
        conceito = "D"
    else:
        conceito = "E"

    print(f'Seu número de identificação é {numeroid}, suas notas foram: primeira nota = {nota1}, segunda nota = {nota2} e terceira nota = {nota3}, a média dos exercícios foi de {me}, a média de aproveitamento foi de {mediaproveitamento} e o conceito correspondente é {conceito}')

    if conceito in ("A", "B", "C"):
        print('Aprovado')
    else:
        print('Reprovado')

    opcao = input("Deseja calcular a nota de outro aluno? (S) sim / N (não)")
    while opcao != "S" and opcao != "N":
        opcao = input('Opção inválida, tente novamente: (S) ou (N) ')

