d = int(input('Distancia da viagem: '))
if d<= 200:
    vc= d*0.50
    print('O custo da sua viagem sera se de {}$'.format(vc))
else:
    vl= d*0.45
    print('O custo da sua viagem sera de {}$'.format(vl))
