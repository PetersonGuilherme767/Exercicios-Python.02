#Ex.0069 - Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No Final, mostre:
#Quantas pessoas tem mais de 18 anos
#Quantos homens foram cadastrados
#Quantas mulheres tem menos de 20 anos

tot20 = 0
totm = 0
tot18 = 0
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totm += 1
    if sexo == 'F' and idade <= 20:
        tot20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break


print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totm} homens cadastrados')
print(f'E temos {tot20} mulheres com menos de 20 anos')







