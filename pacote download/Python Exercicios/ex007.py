nome=input('Digite seu nome :')
n1=int(input('Digite sua primeira nota {}: '.format(nome)))
n2=int(input('Digite sua segunda nota {}: '.format(nome)))
m= (n1+n2)/2
if m >=6 :
    print('Parabens {}, sua media foi {}, voce foi aprovado!!'.format(nome,m))
else:
    print('{} infelizmente sua media foi {}, voce esta reprovado'.format(nome,int(m)))

