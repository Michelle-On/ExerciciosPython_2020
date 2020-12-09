from random import randint
from time import sleep
print('-=-'*5)
print('   JOKENPO')
print('-=-'*5)
ops = ('Pedra','Papel','Tesoura')
print('\033[1;36mSuas opções:\033[m')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
j1=int(input('Qual é a sua \033[1;32mjogada\033[m? '))
jc= randint(0,2)
print('\033[1;35mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!\033[m')
sleep(1)
print('-='*15)
print('O computador escolheu \033[1;31m{}\033[m'.format(ops[jc]))
print('O jogador escolheu \033[1;31m{}\033[m'.format(ops[j1]))
print('-='*15)
if jc == 0:
    if j1 == 0:
        print('\033[1;33mEMPATE\033[m')
    elif j1 == 1:
        print('\033[1;32mO JOGADOR VENCEU!\033[m')
    elif j1 == 2:
        print('\033[1;31mO COMPUTADOR VENCEU\03[m')
elif jc == 1:
    if j1 == 0:
        print('\033[1;31mO COMPUTADOR VENCEU\033[m')
    if j1 == 1:
        print('\033[1;33mEMPATE\033[m')
    if j1 == 2:
        print('\033[1;32mO JOGADOR VENCEU\033[m')
elif jc == 2:
    if j1 == 0:
        print('\033[1;32mO JOGADOR VENCEU\033[m')
    if j1 == 1:
        print('\033[1;31mO COMPUTADOR VENCEU\033[m')
    if j1 == 2:
        print('\033[1;33mEMPATE\033[m')
else:
        print('\033[1;31mJOGADA INVALIDA\033[m')




