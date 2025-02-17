print('Lesson\n')

# Instrukcja break w pętli for z if/else

numbers = [1, 3, 5, 7, 9, 12, 15]
search_for = 12

for num in numbers:
    print(f'Sprawdzam liczbę: {num}')
    
    if num == search_for:
        print('Znaleziono liczbę! Przerywam pętlę')
        break # jeżeli warunek zostanie spełniony, break przerwie działanie pętli

    else: # jeżeli warunek nie zostanie spełniony wykona się instrukcja else
        print(f'Liczba {num} to nie poszukiwana liczba') 

print('Koniec programu')