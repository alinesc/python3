m1 = float(input('Digite a primeira medida (em cm): '))
m2 = float(input('Digite a segunda medida (em cm): '))
m3 = float(input('Digite a terceira medida (em cm): '))
if m2-m3 < m1 < m2 + m3 and m1-m3 < m2 < m1 + m3 and m1-m2 < m3 < m1 + m2:
    print('\033[7;34;40m Essas medidas formam um triângulo.\033[m')
    if m1 == m2 and m2 == m3 and m1 == m3:
        print('Esse é um triângulo equilátero.')
    elif m1 != m2 and m2 != m3 and m1 != m3:
        print('Esse é um triângulo escaleno.')
    else:
        print('Esse é um triângulo isósceles.')
else:
    print('\033[7;31;40m Essas medidas não formam um triângulo.\033[m')