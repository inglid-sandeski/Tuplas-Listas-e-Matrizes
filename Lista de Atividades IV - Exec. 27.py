'''Desenvolva um programa que calcule a soma dos elementos das diagonais principal e secundária de
uma matriz.'''

tamanho = int(input("Digite o tamanho da matriz (NxN): "))
matriz = [[random.randint(1, 9) for _ in range(tamanho)] for _ in range(tamanho)]
print('Matriz:')
for linha in matriz:
    print(" ".join(map(str, linha)))
soma = sum(sum(linha) for linha in matriz)
media = soma / (tamanho * tamanho)
print(f"Soma de todos os números: {soma}")