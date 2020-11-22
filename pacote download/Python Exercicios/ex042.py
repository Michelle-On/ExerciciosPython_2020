#if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2 and r1==r2==r3:
    print('Os segmentos acima \033[1;32mPODEM FORMAR\033[m um triangulo \033[1;36mEQUILÁTERO\033[m')
elif r1<r2+r3 and r2<r1+r3 and r3<r1+r2 and r1==r2 or r2==r1 or r3==r1 or r3==r2:
    print('Os segmentos acima \033[1;32mPODEM FORMAR\033[m um triangulo \033[1;36mISÓSCELES\033[m')
elif r1<r2+r3 and r2<r1+r3 and r3<r1+r2 and r1!=r2!=r3!=r1:
    print('Os segmentos acima \033[1;32PODEM FORMAR\033[m um triangulo \033[1;36mESCALENO\033[m')
else:
    print('Os segmentos acima \033[1;31mNÃO PODEM\033[m formar um triangulo')
