print ('*'*62)#estetica
print('='*20,'Analisando Triagulos','='*20)
print('*'*62)#estetica
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos acima PODEM formar triangulos')
else:
    print('Os segmentos acima NAO PODEM formar triangulos!')