n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n2<n1:
    print('O \033[1;31mPRIMEIRO\033[m valor é maior')
elif n1<n2:
    print('O \033[1;31mSEGUNDO\033[m valor é maior.')
elif n1==n2:
    print('Os dois valores são \033[1;32mIGUAIS\033[m.')
