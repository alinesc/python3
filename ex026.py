"""frase = str(input('Digite uma frase: ')).strip()
print('O número de letras A nessa frase é {}.'.format(frase.lower().count('a')))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.lower().find('a')))
print('A letra A aparece pela última vez na posição {}.'.format(frase.lower().rfind('a')))"""

frase =str(input('Digite uma frase: ')).upper().strip()
print('O número de letras A nessa frase é {}. '.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.find('A')+1)) #somar um para que o usuário considere o início em 1
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.rfind('A')+1))
