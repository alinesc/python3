dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos quilômetros rodados? '))
price = dias * 60 + km * 0.15
print('O valor do aluguel de {} dias, rodando {} quilômetros será de R${:.2f}.'.format(dias, km, price))