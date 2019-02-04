soma = 0
contador = 0
for c in range (1, 500, 2):
    if c % 3 == 0:
        soma += c
        contador += 1
print('A soma no intervalo de {} números é de {}.'.format(contador,soma));

