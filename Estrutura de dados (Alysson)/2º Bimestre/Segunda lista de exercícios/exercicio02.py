"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""
nome = input("Digite seu nome: ")
senha = input("Digite sua senha, não pode ser seu nome: ")
while nome == senha:
    print('Erro , informações inválidas, nome e senha tem que ser diferentes.')
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

print(f"Seu nome é {nome}, e sua senha é {senha}")

