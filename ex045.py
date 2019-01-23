from random import choice
from time import sleep
print('{:=^40}'.format(' JOKENPO '))
nome = input('Nome do jogador: ')
print('''Suas opções: 
[ Pedra ]
[ Papel ]
[ Tesoura ]''')
escolha = input('Qual é a sua jogada? ').strip().upper()
if escolha != 'PEDRA' and escolha !='TESOURA' and escolha != 'PAPEL':
    print('Opção Inválida, tente novamente.')
else:
    escolha_pc = choice(['PEDRA', 'TESOURA', 'PAPEL'])
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!!')
    print('=-' * 20)
    print('O computador jogou {}.'.format(escolha_pc))
    print('{} jogou {}.'.format(nome, escolha))
    print('=-' * 20)
    if escolha_pc == 'PEDRA' and escolha == 'TESOURA' or escolha_pc == 'TESOURA' and escolha == 'PAPEL' or escolha_pc == 'PAPEL' and escolha == 'PEDRA':
        print('O computador venceu.')
    elif escolha_pc == escolha:
        print('O computador jogou {} e você também. Ninguém ganhou nessa rodada.'.format(escolha_pc))
    else:
        print('{} venceu o jogo, parabéns!'.format(nome))
