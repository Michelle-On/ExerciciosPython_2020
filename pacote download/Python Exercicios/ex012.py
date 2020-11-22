preço = float (input('Qual é o preço do produto?? R$ '))
prom = preço - (preço*5/100)
print ('O produto que custava {:.2f}, na promoçao com desconto de 5% vai custar {:.2f}'.format(preço,prom))