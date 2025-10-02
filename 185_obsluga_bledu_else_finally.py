# else - wykona się jeżeli w instrukcji try nie dojdzie do żadnego błędu
# finally - wykona się niezależnie od wystąpienia błędu
import sys

task_per_person = 0

try:
    tasks = 32
    people_str = input('How many people are in the team? ')
    people = int(people_str)

    task_per_person = tasks / people

except ValueError as e:
    print(f'Sorry - you need to enter an integer number / {e}')

except ZeroDivisionError as e:
    print(f'Sorry - you need to enter value > 0 / {e}')

except:
    print(f'Something went wrong: {sys.exc_info() [0]}')

else:
    print(f'Every person should have around {task_per_person} tasks')

finally:
    print('Scripts finished with/without errors')