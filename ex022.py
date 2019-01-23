nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
nomecompleto = len(nome)
numerodeespacos = nome.count(' ')
print('O número de letras do seu nome é {}.'.format(nomecompleto - numerodeespacos))
dividido = nome.split()
print('O primeiro nome tem {} letras.'.format(len(dividido[0])))






