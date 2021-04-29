#Ex.0067 - Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado
#pelo usuário. O programa será interrompido quando o número for negativo.

while True:
    n = int(input('Qual número você quer ver a tabuada?'))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n}x{c}={n*c}')
print('Fim')



