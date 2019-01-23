peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))
IMC = peso / (altura * altura)
print('Seu IMC é de {:.1f} e você está '.format(IMC), end='')
if IMC < 18.5:
    print('abaixo do peso.')
elif IMC < 25:
    print('no peso ideal.')
elif IMC < 30:
    print('com sobrepeso.')
elif IMC < 40:
    print('obeso.')
else:
    print('obeso mórbido.')
