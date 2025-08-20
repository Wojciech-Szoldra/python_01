#Funkcja zwracająca njbliższy dzień roboczy

def give_working_day():
    from datetime import date
    from datetime import timedelta

    day = date.today()

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print(f'working day for {day} is {workingday}')
    return

give_working_day()

print('====LAB====\n')

print('====ZAD 1====\n')

def how_many_days_left():
    from datetime import date
    today = date.today()
    current_year = today.year
    last_day = date(current_year,12,31)
    days_number = last_day - today
    print(f'{days_number.days} days left to the end of the year')
    return

how_many_days_left()

def how_many_weeks_left():
    from datetime import date
    today = date.today()
    current_year = today.year
    last_day = date(current_year,12,31)
    days_number = last_day - today
    print(f'{days_number.days // 7} weeks left to the end of the year')
    return

how_many_weeks_left()