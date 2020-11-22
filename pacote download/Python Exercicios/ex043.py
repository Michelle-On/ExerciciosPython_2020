peso = float(input('Qual é o seu peso? (Kg)'))
alt = float(input('Qual é sua altura? (m)'))
imc = peso/(alt**2)
print('Seu imc é {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce está \033[1;31mABAIXO DO PESO!\033[m')
elif imc <=25:
    print('Voce esta no \033[1;32mPESO IDEAL!')
elif imc <=30:
    print('Voce está em\033[1;35mSOBREPESO!')
elif imc <=40:
    print('Voce esta em \033[1;31mOBESIDADE!')
elif imc >40:
    print('Voce esta em \033[1;31mOBESIDADE MÓRBIDA!')

