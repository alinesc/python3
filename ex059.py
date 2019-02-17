num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro: '))
print('Digite uma das opções a seguir: ')
opcao = 0
while opcao != 5:
    print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair')
    opcao = int(input('Digite aqui a opção desejada: '))
    if opcao == 1:
        print(num1 + num2)
    elif opcao == 2:
        print(num1 * num2)
    elif opcao == 3:
        if num1 > num2:
            print(num1)
        else:
            print(num2)
    elif opcao == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        opcao = int(input('Opção inválida, tente novamente: '))
print('Fim')


