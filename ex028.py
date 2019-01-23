print('Jogo de adivinhação')
from random import randint
from time import sleep
numero = int(input('Digite um número entre 0 e 5: '))
print('Estou lendo o número digitado...')
sleep(4)
sorteio = randint(0,5)
if numero == sorteio:
    print('Parabéns, o número {} foi selecionado pelo computador!'.format(numero))
else:
    print('Infelizmente o número selecionado foi {} e não {}.'.format(sorteio, numero))
print('Fim do jogo!')