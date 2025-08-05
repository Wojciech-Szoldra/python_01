import datetime

# wyświetla minimalną i maksymalną wartość dla roku 
print(f'Minimalna: {datetime.MINYEAR} Maksymalna: {datetime.MAXYEAR}')

print('='*40)

# 1 day, 1:30:00 - Przesuwamy się do przodu. Jeden dzień, dwie godziny i minus 30 minut czyli jeden dzień, jedna godzina i 30 minut.
d1 = datetime.timedelta(days=1, hours=2,minutes=-30)
print(d1)

# -2 days, 21:57:00 - Przesuwamy się do tyłu. Czyli mamy minus dwa dni i plus 21 godzin i 57 minut ponieważ od drugiego dnia odjęliśmy dwie godziny i 3 minuty.
d2 = datetime.timedelta(days=-1,hours=-2,minutes=-3)
print(d2)

# -1 day, 23:27:00 - Wynik sumy. Czyli różnica to 33 minuty.
print(d1+d2)

print('='*40)

# Typ date.
# Utworzenie daty i wyświetlenie osobno jej części
date = datetime.date(1989,9,8)
print(date)
print(date.year)
print(date.month)
print(date.day)

# Dzisiejsza data
print(datetime.date.today())
today1 = datetime.date.today()

print('='*40)

# Poniżej korzystamy z timedelta() i ustalamy za ile dni powinny zostać zapłacone rachunki. Następnie dodajemy do siebie wartości: dzisiejsza data i czas w dniach na zapłacenie rachunków. Wynikiem jest data do której rachunki powinny zostać zapłacone.

today2 = datetime.date.today()
days_to_pay = datetime.timedelta(days=7)
print(f'Today is: {today2}')
print(f'Bills should be paid within: {days_to_pay.days} days')
print(f'The bill should be paid till: {today2 + days_to_pay}')

print('='*40)

# Poniżej korzystamy ze stałej ‘max’, która reprezentuje maksymalną możliwą datę w Pythonie.

end_of_the_world = datetime.date.max
print(type(end_of_the_world))
print(end_of_the_world)
print(end_of_the_world.weekday())

print('='*40)

# Poniżej liczymy ilość dni od wskazanej daty do today()

initial_date = datetime.date(1989,9,8)
current_date = datetime.date.today()
number_of_days = current_date - initial_date
print(f'Number of days: {number_of_days}')

# Odejmując w Pythonie dwie daty otrzymujemy obiekt typu 'timedelta'. Obiekt 'timedelta' ma atrybut 'days', który zwraca liczbę dni jako int

days = number_of_days.days
print(type(days))
number_of_weeks = days / 7
print(f'Number of weeks: {number_of_weeks}')

print('='*40)

# import klasy datetime
from datetime import datetime, timezone

# Typ datetime zwraca datę i czas
print(f'Aktualna data i czas lokalny: {datetime.now()}')
print(f'Aktualna data i czas lokalny: {datetime.today()}')
print(f'UTC (Uniwersalny Czas Koordynowany): {datetime.now(timezone.utc)}')

# Zwracamy numer dnia tygodnia
print(datetime.today().weekday())

print('='*40)

# strftime() konwertuje typ datetime do stringa
date_3 = datetime.now()
print(type(date_3))
print(date_3)
date_4 = datetime.now().strftime("%a")
print(type(date_4))
print(date_4)

print(datetime.now().strftime("%a"))
print(datetime.now().strftime("%A"))
print(datetime.now().strftime("%w"))

# Na przykład potrzebne by było zapisanie do pliku w odpowiednim formacie daty/czasu uruchomienia programu. Możemy wtedy skorzystać z strftime() i sformatować datę według uznania.

print(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

print('====LAB====\n')

print('====ZAD 1====\n')

import math

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02,0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]


print(f'inputdata: {len(inputdata)} / factortable: {len(factortable)}')

# Wersja 1


if len(inputdata) == len(factortable):
    n=0
    for i in inputdata:
        minvalue=inputdata[n]-factortable[n]*inputdata[n]
        print(f'({n}) minvalue: {minvalue} / mininteger: {math.floor(minvalue)}')
        maxvalue=inputdata[n]+factortable[n]*inputdata[n]
        print(f'({n}) maxvalue: {maxvalue} / maxinteger: {math.ceil(maxvalue)}')
        n+=1
else:
    print('inputdata and factor table need to have equal number elements')

# Wersja 2

if len(inputdata) == len(factortable):
    i=0
    while i<len(inputdata):
        minvalue=inputdata[i]-factortable[i]*inputdata[i]
        maxvalue=inputdata[i]+factortable[i]*inputdata[i]
        print('minvalue=',minvalue,'maxvalue=',maxvalue)
        
        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(mininteger,"\t",inputdata[i],"\t",maxinteger)
        i+=1
else:
    print("inputdata and factortable need to have equal number of elements")

print('====ZAD 2====\n')

import random

n=0

for i in inputdata:
    minvalue=inputdata[n]-random.random()*inputdata[n]
    maxvalue=inputdata[n]+random.random()*inputdata[n]
    print(f'({n}) minvalue: {minvalue} / maxvalue: {maxvalue}')
    
    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)
    print(mininteger,"\t",inputdata[n],"\t",maxinteger)
    
    n+=1
else:
    print('inputdata and factor table need to have equal number elements')

print('====ZAD 3====\n')

print(datetime.today())
print(datetime.today().strftime("%Y-%m-%d"))