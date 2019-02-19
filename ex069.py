'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final mostre:
A) quantas pessoas tem mais de 18 anos.
B)Quantos homens foram cadastrados.
C)Quantas mulheres tem menos de 20 anos.
Tem verificacao de sexo válido, e se quer continuar.'''

idade = 0
sexo = ''
continuacao = 'S'
contIdade = 0
contSexo = 0
contMulherVinte = 0
while continuacao == 'S':
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        contIdade += 1
    sexo = input('Digite seu sexo [M/F]: ').strip().upper()
    while True:
        if sexo != 'M' and sexo != 'F':
            sexo = input('Opção inválida, tente novamente: ').strip().upper()
        else:
            break
    if sexo == 'M':
        contSexo += 1
    if idade <= 20 and sexo == 'F':
        contMulherVinte +=1
    continuacao = input('Quer continuar? [S/N] ').strip().upper()
    while True:
        if continuacao != 'S' and continuacao != 'N':
            continuacao = input('Opção inválida, tente novamente: ').strip().upper()
        else:
            break
    if continuacao == 'N':
        break
print(f'Nesse cadastro existem {contIdade} pessoas com 18 anos ou mais; foram cadastros {contSexo} homens e {contMulherVinte} mulheres com 20 anos ou menos.')




