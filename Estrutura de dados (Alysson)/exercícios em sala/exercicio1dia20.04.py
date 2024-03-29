print ('=' *60) 
massa = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = massa / (altura**2)
#ou imc = massa / pow(altura,2)
print (f'IMC calculado {imc}')
if imc < 18.5 :    
    print('Abaixo do peso')
elif imc < 24.9:
    print('Saudável')    
elif imc < 29.9:
    print('Peso em excesso')
elif imc < 34.9:
    print('Obesidade grau 1')
elif imc < 39.9:
    print('Obesidade grau 2 (severa)')
else:
    print('Obesidade grau 3 (mórbida)')

    
