'''Escreva um programa que ordene uma lista de números de forma que os números pares fiquem antes
dos números ímpares, mantendo a ordem original dentro de cada grupo.'''


numeros = [7, 3, 8, 4, 6, 1, 5, 2, 9]

numeros_ordenados = sorted(numeros, key=lambda x: (x % 2 == 0, numeros.index(x)))

print(numeros_ordenados)