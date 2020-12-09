from time import sleep
for n in range(2,51,2):
    print(n, end=' ')
    sleep(0.5)
print('\033[1;31mFim\033[m')
