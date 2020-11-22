print('Informe seu ano de nascimento para saber sua categoria')
ano = int(input('Ano:'))
idd = int(2020-ano)
print('O atleta tem {} anos.'.format(idd))

if idd <= 9:
    print('Sua categoria é \033[1;35mMIRIM!\033[m')
elif idd <= 14:
    print('Sua categoria é \033[1;36mINFANTIL\033[m')
elif idd <= 19:
    print('Sua categoria é \033[1;33mJUNIOR!\033[m')
elif idd <= 25:
    print('Sua categoria é \033[1;32mSÉNIOR!\033[m')
elif idd >25:
    print('Sua categoria é \033[1;31mMASTER!\033[m')