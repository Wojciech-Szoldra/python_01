import random

# Wyświetlenie części znaków z tabeli ASCII
for i in range(32,127):
    print(i, chr(i))

# Funkcja ord() zmienia znak na jego wartość numeryczną Unicode
test = ord('A')
print(f'A in Unicode = {test}')

print()

# Generowanie hasła metoda 1
ints = range(33, 127)
password = ''

for i in range(16):
    password += chr(random.choice(ints))

print(f'Hasło [metoda 1]: {password}')

print()

# Generowanie hasła metoda 2
import secrets
import string

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

print(f'Hasło [metoda 2]: {generate_password(16)}')

print()

# Funkcja os.urandom()
import os

random_bytes = os.urandom(10)
print(f'random_bytes: {random_bytes}')
random_numbers = list(random_bytes)
print(f'bytes to list: {random_numbers}')

# ---Testy---

test1 = string.ascii_letters
print(test1)

test2= string.punctuation
print(test2)

length = 10
alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(length))
print(password)

for i in range(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))

print(password)

# Metoda join()
words = ["Hello", "world", "Python", "is", "awesome"]
sentence = ' '.join(words)
print(sentence)

print('\n===LAB===\n')
print('===Task 1===\n')

min = 1
max = 6

dice = random.randint(min,max)

if dice == 1:
    print('\n o\n')
elif dice == 2:
    print('  o\n\no')
elif dice == 3:
    print('  o\n o\no')
elif dice == 4:
    print('o o\n\no o')
elif dice == 5:
    print('o o\n o\no o')
else:
    print('o o\no o\no o')

print('\n===Task 2===\n')

dices=[] 

for i in range(5):
    roll = random.randint(min,max)
    dices.append(roll)

dices.sort()
print(dices)