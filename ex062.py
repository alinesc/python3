primeiroTermo = int(input('Digite o valor do primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiroTermo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo)
        termo += razao
        cont += 1
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))





