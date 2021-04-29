# Ex.0037 - Escreva um programa que leia um nome inteiro qualquer e peça para o usuário escolherqual será a base de conversão:
# 1 - para Binário
# 2 - para Octal
# 3 - para hexadecimal'''

num = int(input('Digite um número inteiro:'))
print(''''Escolha uma das bases para conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida tente novamente')
