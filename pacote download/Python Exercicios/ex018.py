import math
ang = int(input('Digite o angulo que voce deseja: '))
print('O Angulo {}:'.format(ang))
print('Tem seno {:.2f}'.format(math.sin(math.radians(ang))))
print('Tem cosseno {:.2f}'.format(math.cos(math.radians(ang))))
print('Tem tangente {:.2f}'.format(math.tan(math.radians(ang))))