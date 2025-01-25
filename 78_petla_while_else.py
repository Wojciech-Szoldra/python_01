# Przykład z lekcji

i = 10
i_min = 0

while i >= i_min:
    print(i, 'I like Python')
    i -= 1
else:
    print("Now i =",i)

# Poniższa pętla zostanie przerwana przez instrukcję break - instrukcja else nie zostanie wykonana

licznik = 1

while licznik <= 5:
    print(f'Licznik: {licznik}')
    if licznik == 3:
        print('Pętla została przerwana!')
        break
    licznik += 1
else:
    print('Pętla zakończyła się normalnie')

# Poniższa pętla nie zostanie przerwana przez instrukcję break - wykona się instrukcja else

list1 = [1,2,3,5,7,9]
searched = 4
i = 0

while i < len(list1):
    print(list1[i])
    if list1[i] == searched:
        print(f'Number found: {searched}')
        break
    i += 1
else:
    print(f'Number {searched} not found')

# Funkcja len()

numbers = [1,2,3,4,5]
elements1 = len(numbers)
print(f'Numbers have {elements1} elements')

letters = 'example'
elements2 = len(letters)
print(f'Letters have {elements2} elements')

# *** Pętla while - LAB ***
print('\n*** LAB ***')
print('\nTask 1 - First method\n')

row_number = 1
i = 31

while row_number <= i:
    print(f'Row number {row_number}')
    row_number += 1

print('\nTask 1 - Second method\n')

first_row = 1
last_row = 31
current_row = first_row

while current_row <= last_row:
    print(f'Row number {current_row}')
    current_row += 1

print('\nTask 2\n')

def the_cube_of_number(number1):
    return number1 ** 3

def the_square_root_of_number(number2):
    return number2 ** 0.5

print(the_cube_of_number(3))
print(the_square_root_of_number(9))