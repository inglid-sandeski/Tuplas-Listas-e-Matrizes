'''Diferença entre Listas: Escreva uma função que receba duas listas como entrada e retorne uma nova
lista contendo os elementos que estão presentes apenas em uma das listas, sem repetições.'''

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
set1 = set(lista1)
set2 = set(lista2)
diferenca = set1.symmetric_difference(set2)
lista_diferenca = list(diferenca)
print(lista_diferenca)