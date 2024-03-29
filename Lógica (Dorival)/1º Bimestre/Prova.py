# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 20:40:53 2023

@author: mathe
"""


# Crie um código que gere a tabela verdade para a fórmula:
# (((A^B) v (A^¬C))^(¬A<->D)) <-> (((¬AvE)^(¬E^F))v(¬D^¬F))^(¬BvG)
print ('Testador de fórmula Tabajara: ')
print('(((A^B) v (A^¬C))^(¬A<->D)) <-> (((¬AvE)^(¬E^F))v(¬D^¬F))^(¬BvG)')
print('=' *60)
vetor_Possibilidades = [True , False]
linhas = 0
verdade = 0
mentira = 0
for A in vetor_Possibilidades:
    for B in vetor_Possibilidades:
        for C in vetor_Possibilidades:
            for D in vetor_Possibilidades:
                for E in vetor_Possibilidades:
                    for F in vetor_Possibilidades:
                        for G in vetor_Possibilidades:
                            linhas+=1
                            if (((A and B) or (A and not C)) and (not A == D)) == (((not A or E) and (not E and F ))or(not D and not F))and (not B or G):
                                resultade=True
                                verdade+=1
                            else:
                                resultado=False
                                mentira+=1
                                print(f'A={A}\tB={B}\tC={C}\tD={D}\tE={E}\tF={F}\tG={G}\t Fórmula={resultado}')
print (f'Quantidade de linhas da tabela: {linhas}')
print (f'Quantidade de linhas Verdadeiro: {verdade}')
print(f'Quantidade de linhas Falso: {mentira}') 
                               
                                

