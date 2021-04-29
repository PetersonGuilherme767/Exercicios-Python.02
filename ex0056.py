#Ex.0056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do prograa, mostre:
#A média de idade do gurpo
#Qual é o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos

média = 0
maioridade = 0
nomemaisvelho = ''
menosvinte = 0
for p in range(1, 5):
    print('----- {}ªPessoa -----')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    média = média + idade / 4
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomemaisvelho = nome
        if sexo in 'Mn' and idade > maioridade:
            maioridade = idade
            nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        menosvinte = menosvinte + 1

print('A média de idade do grupo é de {} anos'.format(média))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridade, nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(menosvinte))