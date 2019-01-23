import datetime
sexo = str(input('Digite F para sexo feminino ou M para sexo masculino: ')).strip().capitalize()
if sexo == 'F':
    print('Você está dispensada no alistamento militar obrigatório.')
else:
    data_nascimento = int(input('Digite seu ano de nascimento: '))
    ano_atual = datetime.date.today().year
    diferenca = ano_atual - data_nascimento
    print('Quem nasceu em {} tem {} anos em {}.'.format(data_nascimento, diferenca, ano_atual))
    falta = data_nascimento + 18
    if diferenca < 18:
        pendente = abs(ano_atual - falta)
        print('Ainda faltam {} anos para o alistamento.'.format(pendente))
    elif diferenca > 18:
        passou = ano_atual - falta
        ano_alistamento = data_nascimento + 18
        print('Já se passaram {} anos do seu alistamento. Seu alistamento foi em {}.'.format(passou, ano_alistamento))
    else:
        print('Está na hora de se alistar.')