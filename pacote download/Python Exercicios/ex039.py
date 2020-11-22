ano = int(input('Ano de nascimento: '))
print('Quem nasceu em {} tem {} anos em 2020.'.format(ano,(2020-ano)))
idd = (2020-ano)
if idd<18:
    print('Ainda faltam {} anos para o alistamento'.format(18-idd))
    print('Seu alistamento será em {}.'.format((18-idd)+2020))
elif idd==18:
    print('Voce tem que se alistar \033[1;31mIMEDIATAMENTE!\033[m')
elif idd>18:
    print('Voce já deveria ter se alistado há {} anos'.format(idd-18))
    print('Seu alistamento foi em {}.'.format(2020-(idd-18)))



