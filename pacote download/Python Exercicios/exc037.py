n = int(input('Digite um número inteiro: '))
print('\033[1;35m*-\033[m'*18)
print('Escolha uma das bases de conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
print('\033[1;35m*-\033[m'*18)
opc = int(input('Sua opção: '))


if opc == 1:
    print('{} convertido para BINARIO fica {}'.format(n,bin(n)[2:]))
elif opc == 2:
    print('{} convertido para OCTAL fica {}'.format(n,oct(n)[2:]))
elif opc ==3:
    print('{} convertido para HEXADECIMAL fica {1:}'.format(n,hex(n)[2:]))
else:
    print('\033[1;31mOpção invalida\033[m, tente novamente.')
