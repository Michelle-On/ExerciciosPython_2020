v = (int(input('Qual a velocidade do carro?')))
m = ((v-80)*7)
if v>80:
    print('Voce recebeu uma multa de {}$ por excesso de velocidade (80Km/h).'.format(m))