'''Escreva um código que imprima uma matriz 5x5 com as duas diagonais com números 1 e o restante
da matriz com 0, exceto pelo número central que deve ser 3.'''

tam = 5
matriz = [[0 for _ in range(tam)] for _ in range(tam)]

for i in range(tam):
    matriz[i][i] = 1
    matriz[i][tam - i - 1] = 1
centro = tam // 2
matriz[centro][centro] = 3
for linha in matriz:
    print(" ".join(map(str, linha)))
