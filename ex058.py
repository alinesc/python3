print('Jogo de adivinhação')
cont = 1
from random import randint
from time import sleep
numero = int(input('Digite um número entre 0 e 5: '))
print('Estou lendo o número digitado...')
sleep(4)
sorteio = randint(0,5)
while sorteio != numero:
    cont += 1
    numero = int(input('Não foi dessa vez, tente novamente: '))
print('Você acertou! Foram necessárias {} tentativas.'.format(cont))




