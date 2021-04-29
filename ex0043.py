'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status
de acordo com a tabela abaixo:
abaixo de 18.5:abaixo do peso
entre 18.5 e 25 peso ideal
25 até 30: sobrepeso
30 até 40: obesidade
acima de 40: obesidade morbida'''

peso = float(input('Qual é seu peso?'))
altura = float(input('Qual é sua altura?'))
imc = peso / (altura ** 2)
print('O seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do Peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está com peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está com Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade')
else:
    print('Você esta com Obesidade Morbida')
