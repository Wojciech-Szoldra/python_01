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

words = text.split(' ') # podzieli ze względu na spacje i utworzy tablicę
short_text = ''
counter = 0

for n in words:
    
    short_text += f' {n}'
    counter += 1

    if counter >= 20:
        print(short_text)
        break

print('\nTask 2\n')

definitions = [
    'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
    'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
    'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
    'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.'
    ]

print('\n---ver_1---\n')

counter = 0

for n in range(0,len(definitions)): # niepotrzebnie korzystałem z range i len
    
    short_text2 = ''
    idx = definitions[n]
    words2 = idx.split(' ')

    for m in words2:
        
        short_text2 += f' {m}'
        counter += 1

        if counter >= 20:
            print(f'{short_text2}\n')
            counter = 0
            break

print('\n---ver_2---\n')

for definition in definitions: # do iteracji wystarczy sama lista
 
    words = definition.split(' ')
    short_text = '' # trzeba "czyścić" short_term wewnątrz pętli
    counter = 0
 
    for word in words:
 
        short_text += word+' '
        counter += 1
 
        if counter>=20:
            print(short_text)
            break