"""
Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos. Mostre como resultado se houve lucro, prejuízo ou empate para cada produto. Informe a média de preço de custo e do preço de venda.
"""
produtos = 40
custo = 0
venda = 0
for i in range (produtos):
    preco_custo = float(input(f"Digite o preço de custo do produto {i+1}: R$ "))
    preco_venda = float(input(f"Digite o preço de venda do produto {i+1}: "))
    custo += preco_custo
    venda += preco_venda

    if preco_venda > preco_custo:
        resultado = "Lucro"
    elif preco_venda < preco_custo:
        resultado = "Prejuízo"
    else:
        resultado = "Empate"
    print(f"O produto {i+1} teve {resultado} ")

media_preco_custo = custo / produtos
media_preco_venda = custo / venda
print(f"Média de preço de custo {media_preco_custo}")
print(f"Média de preço de venda {media_preco_venda}")



    

