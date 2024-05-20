'''Escreva um código que imprimirá uma matriz de um tamanho digitado pelo usuário.
Por exemplo tamanho = 5, a matriz será 5x5
• Esta matriz deve ser composta de números aleatórios entre 1 e 9
• Imprima a soma de todos os números
• Imprima a média dos números'''

import random
tamanho = int(input("Digite o tamanho da matriz (NxN): "))
matriz = [[random.randint(1, 9) for _ in range(tamanho)] for _ in range(tamanho)]
print('Matriz:')
for linha in matriz:
    print(" ".join(map(str, linha)))
soma = sum(sum(linha) for linha in matriz)
media = soma / (tamanho * tamanho)
print(f"Soma de todos os números: {soma}")
print(f"Média de todos os números: {media:.2f}")
