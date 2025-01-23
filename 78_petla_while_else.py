licznik = 1

while licznik <= 5:
    print(f'Licznik: {licznik}')
    if licznik == 3:
        print('Pętla została przerwana!')
        break
    licznik += 1
else:
    print('Pętla zakończyła się normalnie')

# Funkcja len()

numbers = [1,2,3,4,5]
elements1 = len(numbers)
print(f'Numbers have {elements1} elements')

letters = 'example'
elements2 = len(letters)
print(f'Letters have {elements2} elements')