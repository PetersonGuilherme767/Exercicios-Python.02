#Ex.0059 - Crie um programa que leia dois valores e mostre um menu. Seu programa deverá realizar a operação
#solicitada em cada caso. [1] Soma. [2] Multiplicar. [3] Maior. [4] Novos Números [5] Sair do programa'''

v1 = int(input('Primeiro valor:'))
v2 = int(input('Segundo valor:'))
opção = 0
while opção != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('>>>> Qual é a sua opção?'))
    if opção == 1:
        print('A soma entra {} + {} é {}'.format(v1, v2, v1 + v2))
    elif opção == 2:
        print('O resultado de {} x {} é {}'.format(v1, v2, v1 * v2))
    elif opção == 3:
        lista = [v1, v2]
        print('Entre {} e {} o maior é {}'.format(v1, v2, max(lista)))
    elif opção == 4:
        print('Informe os números novamente.')
        v1 = int(input('Primeiro valor:'))
        v2 = int(input('Segundo valor:'))
print('Fim do programa! até breve')













