s = float(input('Digite o salario do funcionario: R$ '))
if s>1250:
    print('Quem ganhava R${} passa a ganhar R${:.2f} agora.'.format(s,s+(s*10/100)))
else:
 print('Quem ganhava R${} passa a ganhar R${:.2f} agora'.format(s,s+(s*15/100)))





