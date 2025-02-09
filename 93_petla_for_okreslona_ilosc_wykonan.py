# Utworzenie obiektu range
r = range(5)
print(r)
print(type(r)) # type() zwraca typ danych danego obiektu

print()

# range(stop) - generuje liczby od 0 do stop -1
for i in range(5):
    print(i)

print()

# range(start, stop) - generuje liczby od start do stop -1
for i in range(2, 6):
    print(i)

print()

# range(start, stop, step) - generuje liczby od start do stop - 1, wartość zwiększa się
for i in range(1, 10, 2):
    print(i)

print()

for number1 in range(1,21):
    if number1 %2 == 0: # sprawdza czy liczba jest parzysta, % zwraca resztę
        print('Number %2d is %s' % (number1,'even'))
    else:
        print('Number %2d is %s' % (number1,'odd'))

print()

for number2 in range(1,21):
    if number2 %2 == 0:
        print(f'Number {number2} is even')
    else:
        print(f'Number {number2} is odd')

# *** Pętla wykonywana określoną ilość razy - LAB ***

print('\n*** LAB ***')
print('\nTask 1\n')

string_a = '+---+---+---+---+'
string_b = '|   |   |   |   |'

for i in range(10):
    print(string_a)

print('\nTask 2\n')

for i in range(9):
    if i %2 == 0:
        print(string_a)
    else:
        print(string_b)

print('\nTask 3\n')

x = 'x'

for i in range(9):
    print(x)
    x += 'x'

print('\nTask 4\n')

x = 'xx'
o = 'o'

for i in range(9):
    if i %2 == 0:
        print(o)
        o += 'oo'
    else:
        print(x)
        x += 'xx'

print('\nSecond option\n')

for i in range (1,10):
    if i % 2 == 0:
        print('x' * i)
    else:
        print('o' * i)