# Liste os elementos de uma lista com seus índices usando enumerate().

lista_nomes = ['Maçã', 'Laranja', 'Acerola', 'Acabaxi']

for i, fruta in enumerate(lista_nomes, start=1):
    print(f'{i}. {fruta}')