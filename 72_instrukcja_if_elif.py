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

# *** Instrukcja if / elif - LAB ***

print('\n*** LAB ***\n\nzad_1\n')

likes_min = 500
shares_min = 100

likes = 400
shares = 100

print('Wersja 1')

if likes >= likes_min and shares >= shares_min:
    print('PROMOTION -10%')
else:
    if likes < likes_min:
        print('Not enough likes. You need over 500!')
    else:
        if shares < shares_min:
            print('Not enough shares. You need over 100!')

print('Wersja 2')

if likes < likes_min:
        print('Not enough likes. You need over 500!')
else:
    if shares < shares_min:
            print('Not enough shares. You need over 100!')
    else:
         print('PROMOTION -10%')

print('Wersja 3')

if likes < likes_min:
        print('Not enough likes. You need over 500!')
elif shares < shares_min:
            print('Not enough shares. You need over 100!')
else:
     print('PROMOTION -10%')

print('\nzad_2\n')

pizza_order = False
large_soda_order = False
is_weekend = True

print('wersja_1')
if (pizza_order or large_soda_order) and not is_weekend:
    print('FREE Burger coupon!')
else:
    if not pizza_order and not large_soda_order:
        print('You have to buy pizza or large soda to get the coupon!')
    else:
        if is_weekend:
            print('Come back on non-Weekend day')

print('wersja_2')
if not pizza_order and not large_soda_order:
    print('You have to buy pizza or large soda to get the coupon!')
elif is_weekend:
    print('Come back on non-Weekend day')
else:
     print('FREE Burger coupon!')