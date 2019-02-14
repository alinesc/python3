from math import factorial
numero = int(input('Digite um número para saber seu fatorial: '))
print(factorial(numero))
cont = 1
mult = 1
numero = int(input('Digite um número para saber seu fatorial: '))
while cont < numero:
    fatorial = numero - cont
    mult *= fatorial
    cont = cont + 1
print(numero * mult)


