'''Escreva um programa que ordene uma lista de números de forma que os elementos se alternem entre
o maior e o menor valor. Por exemplo, a lista [1, 3, 5, 7, 9, 2, 4, 6, 8] se tornaria [9, 1, 8, 2, 7, 3, 6, 4,
5].'''

lista_intercalada = []
for i in range(len(lista_ordenada) // 2):
    lista_intercalada.append(lista_ordenada[i])
    lista_intercalada.append(lista_ordenada[-(i + 1)])
if len(lista_ordenada) % 2 != 0:
    lista_intercalada.append(lista_ordenada[len(lista_ordenada) // 2])

print(lista_intercalada)
