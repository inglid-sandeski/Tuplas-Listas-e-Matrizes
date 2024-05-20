'''Escreva um algoritmo que receba duas matrizes como entrada e retorne a soma dessas matrizes, desde
que tenham as mesmas dimensões.'''

matriz1 = [[1, 2, 3], [4, 5, 9]]
matriz2 = [[7, 8, 7], [10, 11, 12]]
if len(matriz1) != len(matriz2) or len (matriz1[0]) != len(matriz2[0]):
    print("As matrizes não têm as mesmas dimensões")
else:
    soma_total = sum(sum(linha) for linha in matriz1) + sum (sum (linha) for linha in matriz2)
    print("0 resultado total das duas matrizes é:", soma_total)
    