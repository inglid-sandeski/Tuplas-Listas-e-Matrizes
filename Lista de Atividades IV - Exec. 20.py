'''Escreva um programa que receba duas tuplas como entrada e retorne uma nova tupla contendo todos
os elementos das duas tuplas, sem repetições.'''

conjunto1 = ('memória ram', 'ssd', 'placa de vídeo', 'software')
conjunto2 = ('ssd', 'placa de vídeo', 'hubspot', 'powerbi')

lista_combinada_sem_duplicatas = []
for item in conjunto1 + conjunto2:
    if item not in conjunto1 or item not in conjunto2:
        lista_combinada_sem_duplicatas.append(item)

num_elementos_unicos = len(set(lista_combinada_sem_duplicatas))
print('A lista sem repetições é', lista_combinada_sem_duplicatas, '!')