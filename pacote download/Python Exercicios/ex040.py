nt1 = float(input('Digite sua 1° nota: '))
nt2 = float(input('Digite sua 2° nota: '))
m = (nt1+nt2)/2

if m < 5:
    print('Sua média é {}, voce está \033[1;31mREPROVADO!\033[m'.format(m))
elif m == 5 or m <= 6.9:
    print('Sua média é {}, voce está de \033[1;36mRECUPERAÇÃO!\033[m'.format(m))
elif m >= 7:
    print('Sua média é {},parabens voce está \033[1;32mAPROVADO!\033[m'.format(m))

