import time

# zwraca ilość sekund, które minęły od 01.01.1970 - początek Unixa
print(time.time())

# localtime() jako parametr przyjmuje czas unixowy i zwraca krotkę (tuple) z datą/czasem
print(time.localtime(time.time()))

# time.asctime() zwraca dzień tygodnia miesiąc dzień godzinę rok
print(time.asctime(time.localtime(time.time())))

# time_perf_counter() precyzyjnie odmierza czas w oparciu o działanie procesora. Jest to czas monotoniczny czyli taki, który zawsze postępuje do przodu i nie może się cofać. Licznik czasu zeruje się po restarcie systemu lub restarcie procesu pythona. Funkcja wykorzystywana jest do robienia benchmarków np. dokładnego mierzenia działania kodu.
start = time.perf_counter()
print(start)

import calendar

print('='*40)
# wyświetlanie kalendarza na określony miesiąc, na każdy dzień przeznaczone jest 5 znaków, a odstępy między liniami mają wynosić 1. Funkcja uruchomiona bez parametrów przyjmie minimalne wartości.
print(calendar.month(2025,7,w=5,l=1))
print('='*40)
# wyznaczamy jaki dzień tygodnia był określonego dnia - pon=0
print(calendar.weekday(2025,7,30))
print('='*40)
# poniższą funkcją zmieniamy dzień od którego wyświetlany jest kalendarz
calendar.setfirstweekday(6)
print(calendar.month(2025,7,w=5,l=1))
print('='*40)
print(f'Czy rok jest przestępny: {calendar.isleap(2025)}')
print('='*40)
# bez 2017
print(f'Ile dni przestepnych jest w określonym zakresie: {calendar.leapdays(2000,2017)}')
print('='*40)
# poniższa funkcja rysuje kalendarz na cały rok
print(calendar.calendar(2025))