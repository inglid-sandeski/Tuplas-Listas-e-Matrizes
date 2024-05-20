''' Escreva um código onde o usuário vai digitar o lado1 e o lado2 do retângulo e imprima este retângulo
em formato de asteriscos'''

lado1 = int(input('Digite o primeiro valor:'))
lado2 = int(input('Digite o segundo valor:'))

for i in range(lado2):
    print('*' * lado1)
    