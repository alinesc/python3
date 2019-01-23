velocidade = int(input('Digite qual a velocidade do carro neste momento (em km/h): '))
print('A velocidade é {}km/h, certo? '.format(velocidade))
if velocidade > 80:
    print('Você excedeu a velocidade, e a sua multa será no valor de R${}. '.format((velocidade - 80)*7))
print('Ok!')