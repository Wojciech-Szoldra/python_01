# Przykładowa instrukcja if

x = 3

if x > 5:
    print('x jest większe od 5')
else:
    print('x jest mniejsze lub równe 5')

# Przykłady z lekcji

age = 27

if age >= 18:
    print('You are adult you can buy alcohol')
else:
    print('You are too young to buy alcohol')

age = 20
is_drunk = True

if age >= 18 and not is_drunk:
    print('You are adult you can buy alcohol')
else:
    print('Sorry, we cannot sell you alcohol')

age = 20
is_drunk = False
is_restricetd_area = False

if age >= 18 and not is_drunk and not is_restricetd_area:
    print('You are adult you can buy alcohol')
else:
    print('Sorry, we cannot sell you alcohol')

# *** Tests ***

is_drunk = False

if not is_drunk:
    print('Jeżeli is_drunk będzie False to warunek się spełni ponieważ zostanie odwrócony = True')
else:
    print('Jeżeli is_drunk będzie True to warunek się nie spełni ponieważ zostanie odwrócony = False')

# *** Instrukcja warunkowa IF - LAB ***

likes = 500
shares = 100

if likes >= 500 and shares >= 100:
    print('PROMOTION -10%')
else:
    print("We haven't reached our goal yet")

pizza = True
large_soda = False
is_weekend = True

if is_weekend and (pizza or large_soda):
    print('You get a coupon for a free hamburger')
else:
    print('Buy a pizza or large drink during the week to receive a coupon.')

disk_size = 140
disk_size_used = 133
file_size = 1

if disk_size >= (disk_size_used + file_size):
    print('Enough space')
else:
    print('Not enough space')