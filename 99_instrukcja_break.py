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

print('\n*** LAB ***')
print('\nTask 1\n')

text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'

words = text.split(' ')
print(words)