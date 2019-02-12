'''maiorPeso = 0
menorPeso = 300
for c in range (1,6):
    peso = float(input('Digite em peso (em kg): '))
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso
print(maiorPeso, menorPeso)'''

for c in range (1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}kg.'.format(maior))
print('O menor peso lido foi {}kg.'.format(menor))