import sys

task_per_person = 0

try:
    tasks = 32
    people_str = input('How many people are in the team? ')
    people = int(people_str)

    task_per_person = tasks / people

except:
    print(f'Something went wrong… {sys.exc_info()}')

print(f'Every person should have around {task_per_person} tasks')