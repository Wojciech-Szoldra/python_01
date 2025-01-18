x = 7

if x > 10:
    print('x jest większe od 10')
elif x > 5:
    print('x jest większe od 5, ale mniejsze lub równe 10')
else:
    print('x jest mniejsze lub równe 5')

age = 22
is_drunk = True
is_restricted_area = False

if age < 18:
    print("You're too young to buy alcohol")
elif is_drunk:
    print('Are you drunk? We cannot sell you alcohol')
elif is_restricted_area:
    print('Restricted area. Alcohol is forbidden')