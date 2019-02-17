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

'''resp = 'S'
soma = quant = média = maior = manor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('A média dos números digitados foi de {:.1f}.'.format(média))
print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))'''