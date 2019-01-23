print('{:=^40}'.format(' LOJAS GUANABARA '))
valor_compra = float(input('Olá! Qual o valor da compra? R$'))
print('Qual será a forma de pagamento? Digite o número referente às seguintes opções: ')
print('[1] à vista dinheiro / cheque')
print('[2] à vista no cartão')
print('[3] em até 2x no cartão')
print('[4] 3x ou mais no cartão')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    opcao1 = valor_compra - valor_compra * 0.1
    print('Você recebeu um desconto de 10% e sua compra sairá por R${:.2f}.'.format(opcao1))
elif opcao == 2:
    opcao2 = valor_compra - valor_compra * 0.05
    print('Você recebeu um desconto de 5% e sua compra sairá por R${:.2f}.'.format(opcao2))
elif opcao == 3:
    opcao3 = valor_compra / 2
    print('O valor das parcelas será de R${:.2f}.'.format(opcao3))
elif opcao == 4:
    opcao4 = int(input('Em quantas parcelas você quer pagar?'))
    valor_total = valor_compra * 0.2 + valor_compra
    valor_parcelado = valor_total / opcao4
    print('Você irá pagar em {} parcelas de R${:.2f}, totalizando R${:.2f} COM JUROS.'.format(opcao4, valor_parcelado, valor_total))
else:
    print('Opçao inválida, tente novamente.')


