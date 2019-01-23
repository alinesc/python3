salario_inicial = float(input('Digite o salário atual: R$'))
if salario_inicial > 1250:
    reajuste_menor = salario_inicial * 0.10 + salario_inicial
    print('O salário passou de {:.2f} para {:.2f}.'.format(salario_inicial, reajuste_menor))
else:
    reajuste_maior = salario_inicial * 0.15 + salario_inicial
    print('O salário passou de {:.2f} para {:.2f}.'.format(salario_inicial, reajuste_maior))