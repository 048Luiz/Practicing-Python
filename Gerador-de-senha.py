"""
---Gerador de Senhas---
O usuário escolhe o tamanho da senha.
O programa gera uma senha aleatória com letras, números e símbolos.
Garante que o primeiro caractere será uma letra maiúscula.
"""

import random
import string

def generate_password(password_size):
    if password_size < 8:
        print('O tamanho mínimo recomendado é de 8 caracteres!')
        return 
    
    password = [
        random.choice(string.digits),
        random.choice(string.punctuation),
        random.choice(string.ascii_lowercase)
    ]
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password += [random.choice(characters) for _ in range(password_size - len(password) - 1)]

    random.shuffle(password)
    
    first_characters = random.choice(string.ascii_uppercase)
    final_password = first_characters + ''.join(password)

    return final_password

print('---Gerador De Senhas---')

try:
    password_size = int(input('Qual o tamanho que deseja a senha: '))
    password = generate_password(password_size)
    if password:
        print(f'Sua senha gerada foi: {password}')

except ValueError:
    print('[ERRO] Digite um número válido!')