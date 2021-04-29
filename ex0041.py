#Ex.0041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimanto de um atleta e mostre
#a sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SÊNIOR
#Acima: MASTER'''

from datetime import date
ano = int(input('Em que ano você nasceu?'))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos'.format(ano, idade))
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade <= 25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')





