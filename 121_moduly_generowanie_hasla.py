import random

# Wyświetlenie części znaków z tabeli ASCII
for i in range(32,127):
    print(i, chr(i))

# Funkcja ord() zmienia znak na jego wartość numeryczną Unicode
test = ord('A')
print(f'A in Unicode = {test}')

print('\n')

# Generowanie hasła metoda 1
ints = range(33, 127)
password = ''

for i in range(16):
    password += chr(random.choice(ints))

print(f'Password is: {password}')

# Generowanie hasła metoda 2

import secrets
import string

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

print(generate_password(16))

# Funkcja os.urandom()
import os

random_bytes = os.urandom(10)
print(random_bytes)
random_numbers = list(random_bytes)
print(random_numbers)