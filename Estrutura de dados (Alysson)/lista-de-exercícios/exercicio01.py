#A velocidade média de um veículo é dado pela expressão Vm= ∆S/∆t, onde: 
#∆S: variação de espaço (ponto de chegada – ponto de partida) em quilômetros
#∆t: variação de tempo (tempo final – tempo inicial) em horas
#Escreva um programa para calcular a velocidade média dada a variação espacial e a variação temporal. 
print ('=' *50) 
variacao_espaco=float(input('Digite quantos quilômetros você percorreu: '))
variacao_tempo=float(input('Digite quantas horas você gastou: '))
velocidade_media = variacao_espaco/variacao_tempo
print (f'A velocidade média é de {velocidade_media:.1f} km/h. ')  


