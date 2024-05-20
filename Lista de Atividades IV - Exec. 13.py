'''Ordenação: Escreva um programa que ordene uma lista de números em ordem crescente ou
decrescente, dependendo do argumento passado para a função.'''

lista = [10, 5, 7, 23, 14, 8]
ordenacao = 'crescente' or 'decrescente'

if ordenacao == 'crescente':
    lista_ordenada = sorted(lista)
elif ordenacao == 'decrescente':
    lista_ordenada = sorted(lista, reverse=True)
else:
    print('Opção de ordenação inválida.')

print('Lista em ordem', ordenacao + ':', lista_ordenada)