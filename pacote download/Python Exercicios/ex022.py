nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiusculo é: ',nome.upper())
print('Seu nome em minusculo é:',nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome)- nome.count(' ')))
#print(('Seu primeiro nome tem {}'.format(nome.find(' '))))
dividido = nome.split()
print('Seu primeiro nome é "{}" e ele tem {} letras'.format(dividido[0],len(dividido[0])))