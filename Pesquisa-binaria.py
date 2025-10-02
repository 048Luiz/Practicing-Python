"""
Testando a pesquisa binária na prática (com passo a passo).
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = int(input('Digite o número que deseja procurar na lista: '))

def pesquisa_binaria(lista, item):
    numero_baixo = 0
    numero_alto = len(lista) - 1
    passo = 1 

    while numero_baixo <= numero_alto:
        numero_meio = (numero_baixo + numero_alto) // 2
        tentativa = lista[numero_meio]

        print(f"[Passo {passo}] baixo={numero_baixo}, alto={numero_alto}, meio={numero_meio}, tentativa={tentativa}")
        passo += 1

        if tentativa == item:
            return numero_meio   
        elif tentativa > item:
            numero_alto = numero_meio - 1
        else:
            numero_baixo = numero_meio + 1
    return None

resultado = pesquisa_binaria(lista, item)

if resultado is not None:
    print(f"O número {item} foi encontrado na posição {resultado} da lista.")
else:
    print(f"O número {item} não foi encontrado na lista.")
