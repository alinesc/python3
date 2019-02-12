somatorioIdade = 0
maisVelho = 0
nomeMaisVelho = ''
idadeMulheres = 0
for c in range (1, 5):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite F para mulher ou M para homem: ').upper().strip()
    somatorioIdade += idade
    if sexo == 'M':
        if maisVelho < idade:
            maisVelho = idade
            nomeMaisVelho = nome
    else:
        if idade <= 20:
            idadeMulheres += 1
media = somatorioIdade / 4
print('A média de idade nesse grupo é de {} anos.'.format(media))
print('A idade do homem mais velho é de {} anos, e o nome dele é {}.'.format(maisVelho, nomeMaisVelho))
if idadeMulheres >=1:
    print('A quantidade de mulheres com menos de 20 anos é de {}.'.format(idadeMulheres))
else:
    print('Não existem mulheres com menos de 20 anos nessa amostra.')
