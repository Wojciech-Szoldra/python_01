line = 'this IS a very STRANGE text'
line1 = 't'

print(line.capitalize()) # wielka pierwsza litera
print(line1.capitalize())

print(line.title()) # każde słowo z wielkiej litery
print(line.upper()) # wszystkie litery wielkie 
print(line.lower()) # wszystkie litery małe
print(line.swapcase()) # odwróci wielkość liter - duże/małe, małe/duże

line2 = 'der Fluß'
print(line2.casefold()) # zmniejszy litery i usunie specyficzne cechy językowe (np. zamieni ‘ß’ na ‘ss’ - nie działa na polskie znaki)

line2 = 'ŻÓŁĆ'
zolc = line2.replace('Ż','Z').replace('Ó','O').replace('Ł','L').replace('Ć','C').lower()
print(zolc)

print(line.count('e')) # liczy wystąpienia - case sensitive
print(line.find('e')) # wskazuje pierwsze wystąpienie od lewej
print(line.rfind('e')) # wskazuje pierwsze wystąpienie od prawej
print(line.index('e')) # działa tak samo jak find(). Różnica jest taka, że w przypadku braku wystąpienia find nie zwraca nic, a index błąd.
print(line.rindex('e'))

print('e' in line) # substring in string - wyrażenie logiczne zwracające true/false

print(line.startswith('this')) # sprawdza czy dany string rozpoczyna się wskazanym ciągiem znaków

print(line.endswith('THIS')) # sprawdza czy dany string kończy się wskazanym ciągiem znaków

import string 

# kilka stałych z modułu string

print(string.ascii_letters) # wszystkie litery alfabetu (małe + wielkie)
print(string.ascii_lowercase) # małe
print(string.ascii_uppercase) # wielkie
print(string.digits) # cyfry 0-9

line4 = 'this is the end of this lesson'
list = line4.split(' ') # rozbije łańcuch znaków na listę -podział według wskazanego znaku
print(list)

text = ' '.join(list) # join() połączy stringi znajdujące się w liście za pomocą znaku/stringa na którym została wywołana
print(text)

print('\n===LAB===\n')
print('===Task 1===\n')

poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''

lines = poem.split('\n')

for i in range(16):
    if i==0:
        print(lines[0])
        continue
    elif i==1:
        print(lines[8])
        continue
    elif i==2:
        print(lines[1])
        continue
    elif i==3:
        print(lines[9])

print('===Lepsza wersja===')

for i in range(8):
    print(lines[i])
    print(lines[i+8])