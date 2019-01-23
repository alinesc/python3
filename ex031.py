distancia = float(input('Qual é a distância da sua viagem? (em km) - '))
if distancia <= 200:
    print('A sua passagem será de R${:.2f}.'.format(distancia * 0.50))
else:
    print('A sua passagem será de R${:.2f}.'.format(distancia*0.45))
