num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro: '))
print('Digite uma das opções a seguir: ')
print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair')
opcao = int(input('Digite aqui a opção desejada: '))
while opcao != 5:
    if opcao == 1:
        print(num1 + num2)
        opcao = int(input('Digite aqui a opção desejada: '))
    elif opcao == 2:
        print(num1 * num2)
        opcao = int(input('Digite aqui a opção desejada: '))
    elif opcao == 3:
        if num1 > num2:
            print(num1)
        else:
            print(num2)
        opcao = int(input('Digite aqui a opção desejada: '))
    elif opcao == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro: '))
        print('Digite uma das opções a seguir: ')
        print('[1] Somar; [2] Multiplicar; [3] Maior; [4] Novos números; [5] Sair')
        opcao = int(input('Digite aqui a opção desejada: '))
print('Fim')

