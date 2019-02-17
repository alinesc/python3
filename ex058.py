'''print('Jogo de adivinhação')
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
print('Você acertou! Foram necessárias {} tentativas.'.format(cont))'''

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10. \nSerá que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Você acertou depois de {} tentativas.'.format(palpites))




