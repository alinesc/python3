'''Faça um programa que mostra a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

numero = cont = 0
while True:
    numero = int(input('Digite o número da tabuada que você quer ver: '))
    if numero < 0:
        break
    cont = 0
    while cont <= 10:
        print(f'{numero} x {cont:2} = {numero * cont}')
        cont += 1
print('FIM!')
