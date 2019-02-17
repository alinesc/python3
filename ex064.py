numero = int(input('Digite um número: '))
somatoria = numero
cont = 0
while numero != 999:
    somatoria += numero
    cont += 1
    numero = int(input('Digite um número: '))
print('Foram digitados {} números e a soma total foi {}.'.format(cont, somatoria))
