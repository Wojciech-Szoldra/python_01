import datetime

# wyświetla minimalną i maksymalną wartość dla roku 
print(datetime.MINYEAR, datetime.MAXYEAR)

# 1 day, 1:30:00 - Przesuwamy się do przodu. Jeden dzień, dwie godziny i minus 30 minut czyli jeden dzień, jedna godzina i 30 minut.
d1 = datetime.timedelta(days=1, hours=2,minutes=-30)
print(d1)

# -2 days, 21:57:00 - Przesuwamy się do tyłu. Czyli mamy minus dwa dni i plus 21 godzin i 57 minut ponieważ od drugiego dnia odjęliśmy dwie godziny i 3 minuty.
d2 = datetime.timedelta(days=-1,hours=-2,minutes=-3)
print(d2)

# -1 day, 23:27:00 - Wynik sumy. Czyli różnica to 33 minuty.
print(d1+d2)

# Dzisiejsza data
print(datetime.date.today())