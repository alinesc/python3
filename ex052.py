cont = 0
numero = int(input('Digite um número: '))
for c in range (1, numero+1):
    if numero % c == 0:
        cont += 1
if cont > 2:
    print('Não é primo.')
else:
    print('É primo.')

