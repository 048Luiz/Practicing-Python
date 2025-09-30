"""
Peça uma palavra e conte quantas vogais ela possui.
"""
palavra = input('Me diga uma palavra: ')
contagem_vogais = 0
vogais = 'aeiou'

for letras in palavra.lower():
     
    if letras in vogais:
        contagem_vogais += 1

print(f'A palavra tem {contagem_vogais} vogais!')