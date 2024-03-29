"""
Ler 80 números e ao final informar quantos número(s) est(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive).
"""
literador = 0
for i in range(80):
    numero = float(input('Digite um número: '))

    if numero >= 10 and numero <= 150:
        literador += 1

print(f'Quantidade de números {literador}')