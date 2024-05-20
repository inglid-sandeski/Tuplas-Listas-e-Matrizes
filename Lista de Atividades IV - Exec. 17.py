'''Desenvolva um programa que remova todos os elementos ímpares de uma lista e imprima a lista
resultante'''

lista = [13, 2, 3, 4, 5, 26, 7, 8, 24, 16]
lista_pares = []

for elemento in lista:
    if elemento % 2 == 0:
        lista_pares.append(elemento)

print('Lista somente com o número pares é:', lista_pares)