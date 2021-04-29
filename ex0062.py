#Ex.0062 - Pergunte ao usuário quantos termos de uma PA ele quer ver. O programa encerra quando ele digitar 0.

primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão da PA:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo = termo + razão
        cont = cont + 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais'))
print('FIM')
