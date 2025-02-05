# Utworzenie obiektu range
r = range(5)
print(r)
print(type(r)) # type zwraca typ danych danego ob8iektu

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
    if number1 %2 == 0:
        print('Number %2d is %s' % (number1,'even'))
    else:
        print('Number %2d is %s' % (number1,'odd'))

print()

for number2 in range(1,21):
    if number2 %2 == 0:
        print(f'Number {number2} is even')
    else:
        print(f'Number {number2} is odd')