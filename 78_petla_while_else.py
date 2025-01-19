licznik = 1

while licznik <= 5:
    print(f'Licznik: {licznik}')
    if licznik == 3:
        print('Pętla została przerwana!')
        break
    licznik += 1
else:
    print('Pętla zakończyła się normalnie')