#Ex.0050 - Desenvolva um programa que leia seis números inteirose mostre a soma apenas dos Pares.
soma = 0
for c in range(1, 7):
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        soma = soma + n
print('A soma dos números pares é {}'.format(soma))
