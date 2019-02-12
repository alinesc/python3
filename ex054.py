from datetime import date
contador = 0
anoAtual = date.today().year
for c in range (1, 8):
    anoNasc = int(input('Digite seu ano de nascimento: '))
    if anoAtual - anoNasc >= 21:
        contador  += 1
print('O número de pessoas com mais de 21 anos é {} e de menores é {}.'.format(contador, 7-contador))