from math import sqrt
n=int(input('Digite um numero: '))
print('\033[1mNumero {}\033[m\n\033[1;31mDobro:{}\033[m\n\033[1;31mTriplo:{}\033[m\n\033[1;31m\033[1;31mRaiz quadrada:{}\033[m'.format(n,(n*2),(n*3),int(sqrt(n))))

