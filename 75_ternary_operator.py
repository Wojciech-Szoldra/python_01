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

# *** IF - LAB ***

print('LAB\n\nzad_1\n')

muscle_pain = False
fever = False
weaknes = False
is_man = False

print('1')

if muscle_pain and fever and weaknes:
    print('Suspicion of influenza')
else:
    print('The flu is unlikely')

print('Suspicion of influenza' if muscle_pain and fever and weaknes else 'The flu is unlikely')

print('2')

if muscle_pain and fever and weaknes:
    print('Suspicion of influenza')
elif weaknes and (not fever or not muscle_pain):
    print('Just take a rest!')
elif muscle_pain or fever:
    print('You may be cold')
else:
    print('The flu is unlikely')

print('3')

if muscle_pain and fever and weaknes:
    print('Suspicion of influenza')
elif is_man and (muscle_pain or fever or weaknes):
    print('Suspicion of influenza')
elif weaknes and (not fever or not muscle_pain):
    print('Just take a rest!')
elif muscle_pain or fever:
    print('You may be cold')
else:
    print('The flu is unlikely')

print('4')

is_check_completed = False

print('CHECK IS COMPLETED' if is_check_completed else 'CHECK NOT DONE YET!')