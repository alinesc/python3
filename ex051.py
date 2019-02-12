termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + 9 * razao
for c in range (termo, decimo + razao, razao):
    print(c,' ⇢ ', end= ' ');
print('ACABOU!')