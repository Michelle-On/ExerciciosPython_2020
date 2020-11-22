from random import randint,choice
print('Escolhendo um numero... espere um momento')
n = (int(input('Estou pensando em um numero de 1 á 30.\n Advinhe o numero: ')))
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
r = choice(lista)

print('Parabens, voce acertou!' if n == r else'Errou kkk, o numero escolhido foi {}'.format(r))