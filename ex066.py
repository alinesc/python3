'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag)
tem que aparecer quantos números foram digitados
'''

numero = cont = soma = 0
while numero != 999:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'Foram digitados {cont} números e a soma total foi de {soma}. ')

'''soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi de {soma}!')
'''



