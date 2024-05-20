'''Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o lançou n
vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de cada face.'''

resultados = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
contagem_ocorrencias = {}
for resultado in resultados:
    contagem_ocorrencias[resultado] = contagem_ocorrencias.get(resultado, 0) + 1

for face, contagem in contagem_ocorrencias.items():
    print(f"Face {face}: {contagem} ocorrência(s)")
