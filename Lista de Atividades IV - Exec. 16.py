'''Escreva um programa que receba duas listas, uma com os valores das notas e outra com os pesos
correspondentes, e calcule a média ponderada.'''

notas = [8.8, 7.8, 6.4, 9]
pesos = [2, 3, 1, 2]

if len(notas) != len(pesos):
    print("As listas de notas e pesos devem ter o mesmo comprimento.")
else:
    soma_produto = 0
    soma_pesos = 0

    for i in range(len(notas)):
        soma_produto += notas[i] * pesos[i]

        soma_pesos += pesos[i]

    media_ponderada = soma_produto / soma_pesos

    print("A média ponderada é:", media_ponderada)