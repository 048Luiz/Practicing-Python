"""
Crie uma lista com todos os números pares de 1 a 50.
"""

lista = []

print('Os números pares de 1 a 50 são:')

for numero in range(1, 51):
      
    if numero % 2 == 0:
        lista.append(numero)

print(lista)