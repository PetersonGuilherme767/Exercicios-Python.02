#Ex.0048 - Faça um programa que leia a soma entre todos os números impares que são multiplos de três
#que se encontram no intervalo de 1 até 500.

soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
print('A soma de todos os valores solicitados é {}'.format(soma))
