#Zwracanie wartości z funkcji (return)
from datetime import date
from datetime import timedelta

def give_working_day(year=date.today().year, 
                     month=date.today().month, 
                     day=date.today().day):

    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    return workingday

#Przypisanie zwróconej wartości do zmiennej
next_work = give_working_day()
print(next_work)

print(give_working_day())