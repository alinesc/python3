'''from math import factorial
numero = int(input('Digite um número para saber seu fatorial: '))
print(factorial(numero))'''


'''cont = 1
mult = 1
numero = int(input('Digite um número para saber seu fatorial: '))
while cont < numero:
    fatorial = numero - cont
    mult *= fatorial
    cont = cont + 1
print(numero * mult)'''


numero = int(input('Digite um número para saber seu fatorial: '))
cont = numero
mult = 1
print('Calculando {}! = '.format(numero), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    mult *= cont
    cont = cont - 1
print(mult)

