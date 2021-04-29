#Ex.0049 - Leia um número e mostre sua tabuada utilizando a estrutura de repetição.

n = int(input('Digite um número:'))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n * c))
