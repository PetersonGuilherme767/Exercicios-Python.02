#Ex.0040 - Crie um programa que leia duas notas de um aluno e calcule sua média
#mostrando uma mensagem no final, de acordo com a média atingida:
#média abaixo de 5.0 REPROVADO
#média entre 5.0 e 6.9 RECUPERAÇÃO
#média 7.0 ou superior APROVADO'''


n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
media = (n1 + n2) / 2
print('Sua média é {:.1f}'.format(media))
if media < 5.0:
    print('REPROVADO.')
elif media > 7.0:
    print('APROVADO')
elif media >=5 and media < 7:
    print('RECUPERAÇÃO')
