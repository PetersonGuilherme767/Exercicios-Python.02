#Ex.0068 - Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido
#quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

v = 0
from random import randint
while True:
    jogador = int(input('Digite um valor:'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o cumputador {computador}. total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar Novamente...')
print(f'GAME OVER!... Você venceu {v} vezes')






