liczba = 5

# Standardowy zapis

if liczba > 0:
    wynik = 'Dodatnia'
else:
    wynik = 'Ujemna'

print(wynik)

# Operator trójargumentowy (ternary operator)

wynik = 'Dodatnia' if liczba > 0 else 'Ujemna'
print(wynik)

it_rains = True

# Standardowy zapis

if it_rains:
    print('we stay at home')
else:
    print('we go out')

# Operator trójargumentowy (ternary operator)

print('we stay at home' if it_rains else 'we go out')