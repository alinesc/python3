'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50,00, R$20,00, R$10 e R$1.00'''

valorSaque = int(input('Digite o valor do saque: R$ '))
cedulas50 = valorSaque // 50
resto50 = (valorSaque % 50)
cedula20 = (resto50 // 20)
resto20 = (resto50 % 20)
cedula10 = (resto20 // 10)
resto10 = (resto20 % 10)
if cedulas50 > 0 and cedulas50 != 1:
    print(f'Você receberá {cedulas50} cédulas de R$50.')
elif cedulas50 == 1:
    print(f'Você receberá {cedulas50} cédula de R$50.')
if cedula20 > 0 and cedula20 != 1:
    print(f'Você receberá {cedula20} cédulas de R$20.')
elif cedula20 == 1:
    print(f'Você receberá {cedula20} cédula de R$20.')
if cedula10 > 0 and cedula10 != 1:
    print(f'Você receberá {cedula10} cédulas de R$10.')
elif cedula10 == 1:
    print(f'Você receberá {cedula10} cédula de R$10.')
if resto10 > 0 and resto10 != 1:
    print(f'Você receberá {resto10} de cédulas de R$1.')
elif resto10 == 1:
    print(f'Você receberá {resto10} de cédula de R$1.')

'''print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break'''

