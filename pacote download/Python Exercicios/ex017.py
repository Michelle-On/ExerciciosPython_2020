from math import hypot
op = float(input('Digite o valor do cateto oposto: '))
ad = float(input('Digite o valor do cateto adjacente: '))
print('A sua hipotenusa vai medir {:.2f}'.format(hypot(op,ad)))
