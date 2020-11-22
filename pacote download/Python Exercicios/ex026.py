frase = str(input('Digite uma frase: ')).strip().upper()
print('Analisando frase...')
print('A letra "A" apareceu {} vezes na frase'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {} '.format(frase.find('A')+1))#+1 apenas para nao ficar o '0'
print('A ultima letra "A" apareceu na posição {}'.format(frase.rfind('A')+1))