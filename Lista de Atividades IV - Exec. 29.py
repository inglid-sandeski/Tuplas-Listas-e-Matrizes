'''Crie um programa que receba uma matriz como entrada e retorne uma lista com as médias de cada
coluna.'''

matriz = [ [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
num_linhas = len(matriz)
num_colunas = len(matriz[0])

medias = []


for j in range(num_colunas):
    soma_coluna = 0

    for i in range(num_linhas):
        soma_coluna += matriz[i][j]

    media_coluna = soma_coluna / num_linhas
    medias.append(media_coluna)
print("Médias das colunas:", medias)