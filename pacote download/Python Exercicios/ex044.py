print('='*20)
print('LOJA MIMAKES STORE')
print('='*20)
pç = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque' )
print('[ 2 ] à vista cartão' )
print('[ 3 ] 2x no cartão' )
print('[ 4 ] 3x ou mais no cartão' )
opc = int(input('Qual é a opção? '))
if opc==1:
    total = pç-(pç*10/100)
elif opc==2:
    total = (pç-(pç*5/100))
elif opc==3:
    total = pç
    parcela = pç/2
    print('Sua compre será parcelada em 2x de R${:.2f}'.format(pç))
elif opc==4:
    total = pç+(pç*20/100)
    ttparcelas = int(input('Quantas parcelas? '))
    parcela = total/ttparcelas
    print('Sua compra sera parcelada e {:.2f}x de R${:.2f} COM juros!'.format(ttparcelas,parcela))
else:
    print('Opção invalida')
    total = 0
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(pç,total))











