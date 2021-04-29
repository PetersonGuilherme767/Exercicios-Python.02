#Ex.0047 - Crie um porgrama que leia todos os números paresque estam no intervalo entre 1 e 50.

for c in range(0, 51, 2):
    print(c)

#Resolução guanabara!

for c in range(1, 51):
    if c % 2 == 0:
        print(c)
