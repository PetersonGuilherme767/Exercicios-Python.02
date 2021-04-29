#Ex.0044 - Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condiçõesde pagamento:
#À VISTA NO DINHEIRO:10%
#À VISTA NO CARTÃO:5%
#EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
#3X OU MAIS NO CARTÃO 20% DE JUROS'''

print('{:=^40}'.format('LOJAS GUANABARA'))
preço = float(input('Preço das compras: R$'))
print('''Formas de Pagamento
[1] à vista no dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = preço / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparcela = int(input('Quantas parcelas?'))
    parcela = total / totalparcela
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totalparcela, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))

