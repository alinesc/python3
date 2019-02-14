sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite o sexo [M/F]: ').strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Informação inválida, tente novamente.')
print('Obrigada pela informação.')

