"""
Peça um número ao usuário e mostre todos os números ímpares de 1 até esse número.
"""
numero = int(input('Diga um número: '))

print('Números ímpares até o número que você digitou:')

for numero in range(1, numero):
    
    if numero % 2 != 0:
        print(f'{numero}')