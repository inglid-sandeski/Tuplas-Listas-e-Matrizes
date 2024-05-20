'''Crie um programa que receba uma lista de palavras e conte quantas vezes cada vogal aparece no total.'''

lista_palavras = ['familia, lar, união, incondicional']
contagem_vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for palavra in lista_palavras:
        for letra in palavra.lower():
         if letra in contagem_vogais:
            contagem_vogais[letra] += 1

print(contagem_vogais)