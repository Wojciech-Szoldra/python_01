import random

# Wyświetlenie części znaków z tabeli ASCII
for i in range(32,127):
    print(i, chr(i))

test = ord('A')
print(f'A in Unicode = {test}')

print('\n')

# Generowanie hasła
ints = range(33, 127)
password = ''

for i in range(16):
    password += chr(random.choice(ints))

print(f'Password is: {password}')