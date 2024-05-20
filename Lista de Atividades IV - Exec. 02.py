'''Escreva um código similar à questão anterior, porém agora a figura deve ser vazia:'''

lado1 = int(input('Digite o comprimento do retângulo:'))
lado2 = int(input('Digite a largura do retângulo:'))

for i in range(lado2) :
     if i == 0 or i == lado2 - 1:
         print('*' * lado1)
     else:
        print('*' + ' ' * (lado1 - 2) + '*')