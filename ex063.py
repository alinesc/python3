'''n = int(input('Quantos números da frequência de Fibonacci você quer ver? '))
F1 = 1
F2 = 1
print(F1)
print(F2)
for c in range (0, n-2):
    soma = F1 + F2
    print(soma)
    F2 = F1
    F1 = soma'''


n = int(input('Quantos números da frequência de Fibonacci você quer ver? '))
F1 = 0
F2 = 1
print(F1 , end=' ')
cont = 1
while cont <= n-1:
    soma = F1 + F2
    print(soma , end=' ')
    F2 = F1
    F1 = soma
    cont += 1
