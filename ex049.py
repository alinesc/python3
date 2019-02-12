numero = int(input('Digite um número pra descobrir sua tabuada: '))
for c in range (0, 11):
    tabuada = numero * c
    print('{} * {} = {}'.format(numero, c, tabuada))