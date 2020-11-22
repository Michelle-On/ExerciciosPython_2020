print('*'*20)
print('EMPRESTIMO BANCARIO')
print('*'*20)
vlimovel = float(input('Digite o valor do imovel: R$'))
sal = float(input('Digite seu salario atual: R$'))
qt = int(input('Digite os anos que deseja financiar: '))
pst = vlimovel/(qt*12)
min = sal *30/100
if pst<=min:
    print('EMPRÉSTIMO APROVADO!')
else:
    print('EMPRÉSTIMO NEGADO!')
print('Para pagar a prestação de um imovel de R${:.2f} em {} anos a prestacão será de R${:.2f}.'.format(vlimovel,qt,pst))

