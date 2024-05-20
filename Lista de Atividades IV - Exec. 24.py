'''Crie um programa que receba uma matriz como entrada e retorne duas listas, uma com a soma dos
elementos de cada linha e outra com a soma dos elementos de cada coluna.'''

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_linhas = [sum(linha) for linha in matriz]

soma_colunas = [sum(coluna) for coluna in zip(*matriz)]

print("Soma das linhas:", soma_linhas)
print("Soma das colunas:", soma_colunas)