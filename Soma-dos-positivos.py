"""
Dada uma lista de números (positivos e negativos), some apenas os positivos.
"""

lista = [20, -5, 12, -16, 8, 12]
positivos = []
negativos = []
soma = 0

for numeros in lista:
    
    if numeros > 0:
        soma += numeros
        positivos.append(numeros)
    else:
        negativos.append(numeros)

print(f'A soma dos números positivos é: {soma}')
print(f'Os números positivos usados na soma foram: {positivos}')
print(f'Os números negativos tirados foram: {negativos}')