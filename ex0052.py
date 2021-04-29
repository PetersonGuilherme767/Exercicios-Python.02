#Ex.0052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número:'))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, total))
if total == 2:
    print('E Por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')