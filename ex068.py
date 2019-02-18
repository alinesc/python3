'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
- digitar o valor, escolher P ou I.  Mostrar o número que foi jogado, o número que o computador escolheu
e o total, mostrando se deu Par ou ímpar.  Escreve se ganhou ou perdeu. * Game over, você venceu x vezes.
Se ganhar, reinicia o jogo.
'''

from random import randint
resultado = ''
cont = 0
ganhou = False
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um número entre 0 e 10: '))
    while jogador != True:
        if jogador < 0 or jogador > 10:
            jogador == False
            jogador = int(input('Opção inválida, tente novamente: '))
        else:
            break
    parOuImpar = input('Você quer par ou ímpar? [P/I]: ').strip().upper()
    while parOuImpar != True:
        if parOuImpar != 'P' and parOuImpar != 'I':
            parOuImpar == False
            parOuImpar = input('Opção incorreta, digite novamente: ').strip().upper()
        else:
            break
    soma = jogador + computador
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(f'Você escolheu {jogador}, {parOuImpar} e o computador escolheu {computador}, totalizando {soma}, que é um número {resultado}.')
    if parOuImpar == 'P' and resultado == 'PAR':
        print('Você acertou!')
        ganhou = True
        cont += 1
    elif parOuImpar == 'I' and resultado == 'ÍMPAR':
        print('Você acertou!')
        ganhou = True
        cont += 1
    else:
        print('Você perdeu :(')
        ganhou = False
    if ganhou == False:
        break
print(f'Game Over! Você ganhou {cont} vezes')

