'''Remover Elemento Específico: Escreva um algoritmo que remova todas as ocorrências de um
elemento específico de uma lista. Portanto, o usuário deverá digitar qual elemento ele gostaria dde retirar
da lista, e o algoritmo deverá substituir cada ocorrência deste número por um asterisco “*”.'''

lista = [1, 2, 3, 4, 5, 2, 2, 6, 7, 2]
print(lista)
elemento_a_remover = int(input("Digite o elemento que você gostaria de remover da lista: "))

for i in range(len(lista)):
    if lista[i] == elemento_a_remover:
        lista[i] = '*'

print(lista)
