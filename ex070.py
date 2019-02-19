'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B)Quantos produtos custam mais de R$1000.
C)Qual é o nome do produto mais barato.'''

somatoriaPreco = 0
acima1000 = 0
resposta = 'S'
menorPreco = 0
maisBarato = ''
while resposta == 'S':
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço: R$'))
    somatoriaPreco += preco
    if preco >= 1000:
        acima1000 =+ 1
    if menorPreco == 0:
        menorPreco = preco
        maisBarato = produto
    elif menorPreco > preco:
        menorPreco = preco
        maisBarato = produto
    print(menorPreco, maisBarato)
    resposta = input('Quer continuar? [S/N]').strip().upper()
    while resposta != 'S' and resposta != 'N':
        resposta = input('Opção inválida, tente novamente: ').strip().upper()
print(f'O total gasto nessa compra foi de R${somatoriaPreco:.2f}; {acima1000} produto(s) custa(m) acima de R$1000,00 e nome do produto mais barato é {maisBarato}.')