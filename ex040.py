nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media < 5.0:
    print('Sua média foi de {:.1f}, abaixo ou igual a 5.0, você está reprovado(a).'.format(media))
elif 5.0 <= media and media <= 6.9:
    print('Sua média foi de {:.1f}, entre 5.0 e 6.9, você está de recuperação.'.format(media))
else:
    print('Sua média foi de {:.1f}, acima de 7.0, você está aprovado.'.format(media))

