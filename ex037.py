numero = int(input('Escreva um número inteiro: '))
print('Digite 1 para conversão para binário')
print('Digite 2 para conversão para octal')
print('Digite 3 para conversão para hexadecimal')
escolha = int(input())
print('Você escolheu a opção {}.'.format(escolha))
if escolha == 1:
    binario = str(bin(numero))
    binario_editado = binario.lstrip('0b')
    print('O número {} em binário é {}.'.format(numero, binario_editado))
elif escolha == 2:
    octal = str(oct(numero))
    octal_editado = octal.lstrip('0o')
    print('O número {} em octal é {}.'.format(numero, octal_editado))
elif escolha == 3:
    hexadecimal = str(hex(numero))
    hexadecimal_editado = hexadecimal.lstrip('0x')
    print('O número {} em hexadecimal é {}.'.format(numero, hexadecimal_editado))
else:
    print('O número digitado é inválido.')
print('Até mais!')

