"""
Leia um número e mostre a tabuada dele de 1 até 10.
"""
numero = int(input('Digite o número que deseja ver a tabuada: '))

print(f'A tabuada dê {numero} é:')

for tabuada in range(1, 11):
    print(f'{numero} x {tabuada:2} = {numero * tabuada:3}')