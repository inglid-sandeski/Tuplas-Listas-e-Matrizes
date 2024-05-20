'''Escreva um programa que verifique se uma matriz é esparsa, ou seja, se a maioria dos seus elementos
é zero.'''

matriz = [
    [0, 0, 0, 0],
    [0, 5, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
num_zeros = sum(row.count(0) for row in matriz)
total_elementos = len(matriz) * len(matriz[0])
if num_zeros > total_elementos / 2:
    print("A matriz é esparsa.")
else:
    print("A matriz não é esparsa.")