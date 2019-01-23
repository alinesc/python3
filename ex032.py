from datetime import date
ano = int(input('Digite um ano qualquer (coloque 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é/foi/será um ano bissexto.'.format(ano))
else:
    print('{} não é/foi/será um ano bissexto.'.format(ano))