#Ex.0039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade
#se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se ja passou do tempo do alistamento
#seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

'''ano = int(input('Ano de nascimento:'))
idade = 2020 - ano
print('Quem nasceu em {} tem {} anos em 2020'.format(ano, idade))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
    print('Seu alistamento será em {}'.format(18 - idade + 2020))
elif idade > 18:
    print('Você ja deveria ter se alistado há {} anos'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(2020 - (idade - 18)))
else:
    print('Você deve se alistar IMEDIATAMENTE!')'''

from datetime import date
ano = int(input('Ano de Nascimento:'))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade < 18:
    print('Seu Alistamento será em {}'.format(ano + 18))
elif idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(atual - (idade - 18)))
