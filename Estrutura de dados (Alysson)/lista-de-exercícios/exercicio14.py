#A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de bolos a cada dia. Cada pãozinho custa R$ 0,12 e o pedaço de bolo custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e bolos (juntos), e quanto' deve guardar numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de bolos vendidos, e depois calcular quanto arrecadou naquele dia e quanto deve guardar na poupança.
print ('=' *50)
paes_vendidos = int(input('Quantos pães foram vendidos no dia? '))
bolos_vendidos = int(input('Quantos bolos foram vendidos no dia? '))
quantidade_paes = paes_vendidos * 0.12
quantidade_bolos = bolos_vendidos * 1.50
arrecadacao_dia = quantidade_paes + quantidade_bolos
poupanca = arrecadacao_dia * 0.10
print (f'A quantidade de pães vendidos foram de {paes_vendidos} pães , a quantidade de bolos vendidos foram de {bolos_vendidos} bolos , a arrecadação do dia foi de R${arrecadacao_dia:.2f} e deve-se guardar na poupança R${poupanca:.2f}')




