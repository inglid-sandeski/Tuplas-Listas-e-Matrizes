'''Escreva um algoritmo que encontre e retorne o maior elemento em uma lista de números.'''

numeros = [13, 5, 5, 24, 16, 8]
maior_numero = numeros[0]
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero

print("O maior elemento na lista é:", maior_numero)
