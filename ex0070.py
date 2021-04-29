#Ex.0070 - Crie um programa que leia o nome e o preço de varios produtos.
#O programa deverá perguntar se o usuário vai continuar. No final, Mostre:
# Qual é o total gasto na compra
# Quantos produtos custam mais de R$1000
# Qual é o nome do produto mais barato

produto = 0
total = 0
cont = 0
menor = 0
barato = ' '
while True:
    nome = str(input('Nome do Produto:'))
    preco = int(input('Preço R$:'))
    cont += 1
    total += preco
    continuar = ' '
    if preco >= 1000:
        produto += 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Valor total é {total:.2f}')
print(f'Temos {produto} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}')



