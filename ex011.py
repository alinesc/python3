alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
are = alt * lar
tin = are / 2
print('A área da parede é {}m2 e a quantidade de tinta necessária é de {:.2f}L.'.format(are, tin))
