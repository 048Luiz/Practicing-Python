"""
Peça 5 números ao usuário, armazene em uma lista e mostre o maior e o menor.
"""
lista = []

for _ in range(5):
    numero = int(input('Digite um número: '))
    lista.append(numero)

print(f'O maior número é: {max(lista)}')
print(f'O menor número é: {min(lista)}')

