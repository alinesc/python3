print('-----SIMULADOR DE EMPRÉSTIMO IMOBILIÁRIO-----')
valor_casa = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual o salário do comprador? R$'))
tempo_pagamento = int(input('Em quantos anos deseja pagar? '))
tempo_mensal = tempo_pagamento*12
if valor_casa/tempo_mensal <= 0.3 * salario:
    print('O seu empréstimo está aprovado e o valor da parcela será de R${:.2f}'.format(valor_casa/tempo_mensal))
else:
    print('O valor da prestação excede sua capacidade de pagamento, que é de 30% do seu salário. Seu empréstimo foi negado.')

