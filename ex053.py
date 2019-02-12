frase = input('Digite uma frase: ').strip().upper()
fraseSemEspaco = frase.replace(' ', '')
quantidade = len(fraseSemEspaco)
contrario = ''
for c in range (quantidade-1, -1, -1):
    contrario += fraseSemEspaco[c]
if fraseSemEspaco == contrario:
    print('Essa frase é um palíndromo, pois {} é igual a {}.'.format(fraseSemEspaco, contrario))
else:
    print('Essa frase é não é um palíndromo, pois {} não é igual a {}.'.format(fraseSemEspaco, contrario))

'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
    
ou após o join:

inverso = junto[::-1] - sem usar o for


    
'''
