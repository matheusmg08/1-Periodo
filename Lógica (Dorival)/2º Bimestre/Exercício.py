possibilidade= [True, False]
verdadeiro1= 0
verdadeiro2= 0
verdadeiro3= 0
falso1= 0
falso2= 0
contador1 = 0
contador2 = 0
contador3 = 0
lista1= []
lista2= [] 
qtd= int(input('A fórmula tem 2 ou 3 variáveis: '))
while qtd != 2 and qtd != 3:
    qtd= int(input('Quantidade informada é invalida, digite 2 ou 3 variáveis: '))

if qtd == 2:
    
    print ('Para melhor funcionamento utilize os termos "a" e "b" (minúsculos)')
    formula1= input('Digite a primeira fórmula em notação Python: ')
    formula2= input('Digite a segunda fórmula em notação Python: ')
    
    for a in possibilidade:
        for b in possibilidade:
            contador1 +=1
            if eval(formula1):
                resultado = True
                verdadeiro1 +=1
            else:
                resultado = False
                falso1 +=1 
            print (f'A = {a} \t B = {b} \t Resultado = {resultado}')
            lista1.append(resultado)
    print (f'A Tabela tem {contador1} linhas.')
    print (f'A tabela tem {verdadeiro1} linhas verdadeiras.')
    print (f'A tabela tem {falso1} linhas falsas.')

    if contador1 == verdadeiro1:
        print('A tabela é TAUTOLOGICA.')
    elif contador1 == falso1:
            print('A tabela é CONTRADITÓRIA.')
    else:
            print('A tabela é SATISFATÓRIA.')
    print ('-'*30)
    
    for a in possibilidade:
        for b in possibilidade:
            contador2 +=1
            if eval(formula2):
                resultado = True
                verdadeiro2 +=1
            else:
                resultado = False
                falso2 +=1 
            print (f'A = {a} \t B = {b} \t Resultado = {resultado}')
            lista2.append(resultado)
    print (f'A Tabela tem {contador2} linhas.')
    print (f'A tabela tem {verdadeiro2} linhas verdadeiras.')
    print (f'A tabela tem {falso2} linhas falsas.')
    if contador2 == verdadeiro2:
        print('A tabela é TAUTOLOGICA.')
    elif contador2 == falso2:
        print('A tabela é CONTRADITÓRIA.')
    else:
        print('A tabela é SATISFATÓRIA.')
    print ('-'*30)
    if lista1 == lista2:
        print('As fórmulas são equivalentes.')
    else:
        print('As fórmulas não são equivalentes.')
    
    
    
if qtd == 3:
    
    print ('Para melhor funcionamento utilize os termos "a" e "b" (minúsculos)')
    formula1= input('Digite a primeira fórmula em notação Python: ')
    formula2= input('Digite a segunda fórmula em notação Python: ')
    
    for a in possibilidade:
        for b in possibilidade:
            for c in possibilidade:
                contador1 +=1
                if eval(formula1):
                    resultado = True
                    verdadeiro1 +=1
                else:
                    resultado = False
                    falso1 +=1 
                print (f'A = {a} \t B = {b} \t C = {c} \t Resultado = {resultado}')
                lista1.append(resultado)
    print (f'A Tabela tem {contador1} linhas.')
    print (f'A tabela tem {verdadeiro1} linhas verdadeiras.')
    print (f'A tabela tem {falso1} linhas falsas.')

    if contador1 == verdadeiro1:
        print('A tabela é TAUTOLOGICA.')
    elif contador1 == falso1:
        print('A tabela é CONTRADITÓRIA.')
    else:
        print('A tabela é SATISFATÓRIA.')
    print ('-'*30)
    
    for a in possibilidade:
        for b in possibilidade:
            for c in possibilidade:
                contador2 +=1
                if eval(formula2):
                    resultado = True
                    verdadeiro2 +=1
                else:
                    resultado = False
                    falso2 +=1 
                print (f'A = {a} \t B = {b} \t C = {c} \t Resultado = {resultado}')
                lista2.append(resultado)
    print (f'A Tabela tem {contador2} linhas.')
    print (f'A tabela tem {verdadeiro2} linhas verdadeiras.')
    print (f'A tabela tem {falso2} linhas falsas.')
    if contador2 == verdadeiro2:
        print('A tabela é TAUTOLOGICA.')
    elif contador2 == falso2:
        print('A tabela é CONTRADITÓRIA.')
    else:
        print('A tabela é SATISFATÓRIA.')
    
    if lista1 == lista2:
        print('As fórmulas são equivalentes.')
    else:
        print('As fórmulas não são equivalentes.')
    print ('-'*30)
    if lista1 == lista2:
        print('As fórmulas são equivalentes.')
    else:
        print('As fórmulas não são equivalentes.')