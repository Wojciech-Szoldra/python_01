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