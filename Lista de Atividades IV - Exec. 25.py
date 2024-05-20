'''Escreva um programa que substitua todos os elementos de uma matriz por um valor especificado pelo
usuário.'''

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz atual:")
for linha in matriz:
    print(linha)
novo_valor = int(input("Digite o novo valor para substituir todos os elementos da matriz: "))
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = novo_valor
print("Matriz atualizada:")
for linha in matriz:
    print(linha)