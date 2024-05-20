'''Crie um programa que receba uma tupla de números e retorne duas tuplas, uma contendo os números 
pares e outra os números ímpares.'''

numtup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numpar = tuple(num for num in numtup if num % 2 == 0)
numinpar = tuple(num for num in numtup if num % 2 != 0)
print('os numeros pares são:', numpar)
print('os numeros impares são:', numinpar)