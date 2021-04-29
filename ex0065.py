#Ex.0065 - Crie um programa que leia vários números inteiros. No final da execução, mostre
#a média entre todos os valores e qual foi o maior e o menor entre eles. O programa
#deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

menor = 0
maior = 0
soma = 0
média = 0
cont = 0
opção = 'S'
while opção == 'S':
    num = int(input('Digite um número:'))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


    média = soma / cont
    opção = str(input('Quer continuar?')).upper().strip()
    if opção == 'N':
        print('Você digitou {} números'.format(cont))
        print('A média entre eles foi {}'.format(média))
        print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
print('Acabou')

