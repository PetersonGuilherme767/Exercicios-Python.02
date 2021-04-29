#Ex.0064 - Crie um programa que leia vários números inteiros.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitador e qual foi a soma entre eles.

soma = 0
cont = 0
n = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]:'))
    cont += 1
    soma += n
print('Você Digitou {} números e a soma entre eles é {}'.format(cont - 1, soma - 999))

