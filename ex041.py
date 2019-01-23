from datetime import date
ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade <= 9:
    print('Você tem {} anos e pertence à categoria MIRIM.'.format(idade))
elif idade >9 and idade <= 14:
    print('Você tem {} anos e pertence à categoria INFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos e pertence à categoria JUNIOR.'.format(idade))
elif idade > 19 and idade <= 25:
    print('Você tem {} anos e pertence à categoria SÊNIOR.'.format(idade))
else:
    print('Você tem {} anos e pertence à categoria MASTER.'.format(idade))