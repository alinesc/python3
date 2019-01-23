import math
angulo = float(input('Digite um ângulo: '))
conversao = math.radians(angulo)
print('Em relação ao ângulo {}, os valores de seno, cosseno e tangente são, respectivamente: {:.2f}, {:.2f}, {:.2f}.'.format(angulo, math.sin(conversao), math.cos(conversao), math.tan(conversao)))

