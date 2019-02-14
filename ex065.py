somatoria = 0
cont = 0
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))
if numero1 > numero2:
    maiorValor = numero1
else:
    maiorValor = numero2
if numero1 < numero2:
    menorValor = numero1
else:
    menorValor = numero2
if numero1 == numero2:
    maiorValor = numero1
    menorValor = numero1
opcao = input('Quer continuar? [S/N] ').strip().upper()
if opcao != 'S' and opcao != 'N':
    opcao = input('Opção inválida, tente novamente: ').strip().upper()
while opcao == 'S':
    numero3 = int(input('Digite um número: '))
    somatoria += numero3
    cont += 1
    if numero3 >= maiorValor:
        maiorValor = numero3
    if numero3 <= menorValor:
        menorValor = numero3
    opcao = input('Quer continuar? [S/N] ').strip().upper()
    if opcao != 'S' and opcao != 'N':
        opcao = input('Opção inválida, tente novamente: ').strip().upper()
numerosdigitados = 2 + cont
media = (numero1 + numero2 + somatoria) / numerosdigitados
print('A média dos números digitados foi de {:.1f}.'.format(media))
print('O maior número digitado foi {} e o menor foi {}.'.format(maiorValor, menorValor))
