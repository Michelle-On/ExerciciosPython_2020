n=int(input('\033[1;mDigite um numero qualquer: \033[m'))
s= n+1
a= n-1
print('\033[1;mO sucessor do numero\033[m \033[1;31m{}\033[m \033[1mé\033[m :\033[1;32m{}\033[m, \033[1;me o seu antecessor é\033[m :\033[1;32m{}\033[m'.format(n,s,a))

#ou
#print('O sucessor do numero {} é {}, e o seu antecessor é {}'.format(n,(n+1),(n-1)))
