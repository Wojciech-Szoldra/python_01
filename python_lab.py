print('---1. Typy danych---')

num1 = 2
print(type(num1))
str_num = str(num1)
print(type(str_num))

print('---2. Input---')

'''
def multiplication():
    number_1 = input('Enter first number: ')
    number_2 = input('Enter second number: ')
    result = int(number_1) * int(number_2)
    return print(f'Result: {result}')

multiplication()
'''

print('---3. Struktury danych---')

hp = ['KF','KT','WA','CZO','ZF','KP','IŚ']
print(hp)
print(hp[2]) #indeksujemy od zera
hp.append('NEW1') #dodajemy na końcu
print(hp)
hp.insert(1,'NEW2') #dodajemy na wskazanym indeksie
print(hp)
hp.remove('NEW1')
print(hp)
hp.sort() #sortujemy listę - nie zwraca nowej
print(hp)
list1 = [2,6,8,3,4]
list2 = sorted(list1) #sortujemy listę - zwraca nową
print(list2)

print('---4. Krotki---')

# krotki są niemutowalne - nie da się zmienić ich zawartości

tuple1 = (1,2,3,4,5)
print(tuple1[1])
print(tuple1.index(3)) # wskazuje na jakim indeksie znajduje się element
print(max(tuple1)) # zwraca największy element
tuple_to_list = list(tuple1) # konwersja krotki na listę
tuple_to_list.append(6)
print(tuple_to_list)

print('---5. Słowniki---')

country_leaders = {'PL':'Duda','US':'Trump'}
print(country_leaders)
print(country_leaders['PL']) # dostęp do wartości przez klucz
country_leaders['DE'] = 'Merkel'
print(country_leaders)
print(country_leaders.keys())

print('---6. Instrukcja warunklowa if---')

def check_number(num):
    if num > 0:
        print('liczba jest dodatnia')
    elif num == 0:
        print('liczba jest równa zero')
    else:
        print('liczba jest ujemna')

check_number(5)
check_number(0)
check_number(-3)

liczba = -5
ternary = 'dodatnia' if liczba > 0 else 'ujemna'
print(ternary)

print('---7. Pętle for i while---')

licznik = 1

while licznik <= 5:
    print(f'Licznik wynosi: {licznik}')
    licznik+=1

liczby = [1,2,5,7,9,10]
szukana = 5
i = 0

print(len(liczby))

while len(liczby) > i:
    if szukana == liczby[i]:
        print(f'Szukana liczba to: {szukana}')
        break
    i+=1
    print(i)

print('\n===range()===\n')

print("=== PRZYKŁAD 1: range(5) ===")
print("Wypisujemy liczby od 0 do 4:")
for i in range(5):
    print(f"Liczba: {i}")

print("\n" + "="*40 + "\n")

print('\n===moduł string===\n')

import string

tekst = "Telefon: +48 123-456-789, adres e-mail example@example.com"
# pętla przejdzie przez wszystkie znaki, 
# znak trafi do 'wynik' jeżeli spełniony będzie warunek if
wynik = ''.join(ch for ch in tekst if ch in string.digits) 
print(wynik)

print(string.ascii_letters)

line = 'this is the end of this lesson'
list = line.split(' ')
print(list)

# funkcja join() połączy stringi znajdujące się w liście 
# za pomocą znaku/stringa na którym została wywołana
text = ' '.join(list) 
print(text)

print('='*40)

import random

moneta = random.randint(1,2)
wynik = 'orzeł' if moneta == 1 else 'reszka'
print(f'Orzeł czy Reszka? {wynik}')

print('='*40)

liczby = [1,2,3,4,5,6,7,8,9]

# Slicing

# Wyciągamy 3 pierwsze elementy
t1 = liczby[0:3]
print(t1)

# Wyciągamy wszystko od drugiego elementu
t2 = liczby[1:]
print(t2)

# Wyciągamy dwa pierwsze elementy
t3 = liczby[:2]
print(t3)

# Wyciągamy ostatnie trzy elementy
t4 = liczby[-3:]
print(t4)