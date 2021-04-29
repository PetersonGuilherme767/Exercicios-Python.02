#Ex.0036 - Escreva um programa para aprovar o empréstimo bancário para a compra
#de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele
#vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
#ou então o empréstimo será negado.

print('\033[34mOlá, Seja Bem-Vindo!\033[m')
casa = float(input('Qual o valor do imóvel R$?'))
salario = float(input('Qual é o seu salário atual?'))
anos = float(input('Em quantos anos deseja pagar o imóvel?'))
prestaçao = casa / anos / 12
if prestaçao < salario * 30 /100:
    print('\033[32mSeu financiamento foi APROVADO!\033[m')
    print('Sua prestação será R${:.2f}'.format(prestaçao))
else:
    print('\033[31mInfelizmente seu Financiamento foi Reprovado\033[m')

