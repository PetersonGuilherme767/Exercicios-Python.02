#Ex.0055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso.

lista = []
for c in range(1, 6):
    peso = float(input('Peso da {} pessoa:'.format(c)))
    lista = lista + [peso]
print('O maior peso foi:', max(lista))
print('O menor peso foi:', min(lista))
