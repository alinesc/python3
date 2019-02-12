soma = 0
cont = 0
for c in range (1, 7):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('O resultado da soma dos {} números pares digitados é {}.'.format(cont, soma))