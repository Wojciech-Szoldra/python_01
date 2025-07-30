import time

print(time.time())

print(time.localtime(time.time()))

print(time.asctime(time.localtime(time.time())))

start = time.perf_counter()
print(start)

import calendar

print('='*40)
print(calendar.month(2025,7,w=5,l=1))
print('='*40)
print(calendar.weekday(2025,7,30))
print('='*40)
calendar.setfirstweekday(6)
print(calendar.month(2025,7,w=5,l=1))
print('='*40)
print(f'Czy rok jest przestępny: {calendar.isleap(2025)}')
print('='*40)
# bez 2017
print(f'Ile dni przestepnych jest w określonym zakresie: {calendar.leapdays(2000,2017)}')
print('='*40)
print(calendar.calendar(2025))