#Ex.0058 - O computador vai pensar em um número de 0 a 10. O jogador vai tentar adivinhar até acertar
#mostrando no final quantos palpites foram necessário para vencer'''

from random import randint
computador = randint(0, 10)
print('Pensei em um número entre 0 e 10, tente adivinhar!')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos, tente mais uma vez.')
print('Acertou com {} tentativas, Parabéns!!'.format(palpite))


