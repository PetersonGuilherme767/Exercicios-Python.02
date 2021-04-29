#Ex.0042 - Mostre o tipo de triângulo que será formado:
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes.

r1 = float(input('Primeiro Seguimento:'))
r2 = float(input('Segundo Seguimento:'))
r3 = float(input('Terceiro Seguimento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Esses Seguimentos podem formar um Triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Esses Seguimentos não podem formar um Triângulo')