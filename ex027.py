nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('Seu primeiro nome é {} e seu último nome é {}.'.format(dividido[0], dividido[len(dividido)-1]))

