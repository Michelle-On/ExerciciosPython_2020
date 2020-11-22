nome = input('Digite seu nome: ')
salario = int (input('Digite seu salario atual: R$'))
promocao = salario + (salario*15/100)
print('Parabéns {}, voce recebeu uma promoção de 15% no seu salario, de {}R$ para {}R$'.format(nome,salario,promocao))